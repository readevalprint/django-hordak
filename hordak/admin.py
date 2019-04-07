from django.contrib import admin
from django.db import transaction as db_transaction
from django import forms
from django.db.models import Sum

from django.utils.safestring import mark_safe
from mptt.admin import MPTTModelAdmin

from hordak.models import TransactionCsvImportColumn, TransactionCsvImport
from . import models
from django.urls import reverse


def create_river_button(obj, transition_approval, view_name):
    approve_ticket_url = reverse(
        view_name,
        kwargs={
            "uuid": str(obj.uuid),
            "next_state_id": transition_approval.destination_state.pk,
        },
    )
    return f"""
        <input
            type="button"
            style="margin:2px;2px;2px;2px;"
            value="{transition_approval.source_state} -> {transition_approval.destination_state}"
            onclick="location.href=\'{approve_ticket_url}\'"
        />
    """


@admin.register(models.Account)
class AccountAdmin(MPTTModelAdmin):
    list_display = ("name", "code_", "type_", "balance", "uuid")

    search_fields = ["uuid"]

    def code_(self, obj):
        if obj.is_leaf_node():
            return obj.full_code or "-"
        else:
            return ""

    def type_(self, obj):
        return models.Account.TYPES[obj.type]


class LegInline(admin.TabularInline):
    model = models.Leg
    extra = 0
    autocomplete_fields = ["account"]


@admin.register(models.Transaction)
class TransactionAdmin(admin.ModelAdmin):
    search_fields = ["uuid"]

    list_display = [
        "pk",
        "timestamp",
        "debited_accounts",
        "total_amount",
        "credited_accounts",
        "uuid",
    ]
    readonly_fields = ("timestamp",)
    inlines = [LegInline]

    def debited_accounts(self, obj):
        return ", ".join([str(leg.account) for leg in obj.legs.debits()]) or None

    def credited_accounts(self, obj):
        return ", ".join([str(leg.account) for leg in obj.legs.credits()]) or None

    def total_amount(self, obj):
        return obj.legs.debits().aggregate(Sum("amount"))["amount__sum"]


@admin.register(models.Deposit)
class DepositAdmin(TransactionAdmin):
    list_display = [
        "pk",
        "timestamp",
        "debited_accounts",
        "total_amount",
        "credited_accounts",
        "uuid",
        "status",
        "river_actions",
    ]

    def get_list_display(self, request):
        self.user = request.user
        return super().get_list_display(request)

    def river_actions(self, obj):
        content = ""
        for transition_approval in obj.river.status.get_available_approvals(
            as_user=self.user
        ):
            content += create_river_button(obj, transition_approval, "approve_deposit")

        return mark_safe(content)


@admin.register(models.Withdraw)
class WithdawAdmin(TransactionAdmin):
    list_display = [
        "pk",
        "timestamp",
        "debited_accounts",
        "total_amount",
        "credited_accounts",
        "uuid",
        "status",
        "river_actions",
    ]

    def get_list_display(self, request):
        self.user = request.user
        return super().get_list_display(request)

    def river_actions(self, obj):
        content = ""
        for transition_approval in obj.river.status.get_available_approvals(
            as_user=self.user
        ):
            content += create_river_button(obj, transition_approval, "approve_withdraw")

        return mark_safe(content)


@admin.register(models.Leg)
class LegAdmin(admin.ModelAdmin):
    list_display = ["id", "uuid", "transaction", "account", "amount", "description"]
    autocomplete_fields = ["transaction"]


@admin.register(models.StatementImport)
class StatementImportAdmin(admin.ModelAdmin):
    readonly_fields = ("timestamp",)


@admin.register(models.StatementLine)
class StatementLineAdmin(admin.ModelAdmin):
    readonly_fields = ("timestamp",)


class TransactionImportColumnInline(admin.TabularInline):
    model = TransactionCsvImportColumn


@admin.register(TransactionCsvImport)
class TaskMetaAdmin(admin.ModelAdmin):
    list_display = ["id", "uuid", "state", "timestamp", "has_headings"]
    inlines = [TransactionImportColumnInline]
