from django.db.models import Queryset, Manager, Subquery, OuterRef

from tablechangelogger.models import TableChangesLog


class TableChangesLogQueryset(Queryset):
    def add_latest_log_time(self, **kwargs):
        nonempty_kwargs = {key: value for key, value in kwargs.items()
                           if value is not None}
        if 'instance_id' in nonempty_kwargs.keys():
            nonempty_kwargs['instance_id'] = OuterRef('id')

        query = (TableChangesLog.objects.filter(**(nonempty_kwargs).
                                                order_by('-created_at').
                                                values('created_at')[:1]))
        return self.annotate(latest_log_time=Subquery(query))


class TableChangesLogManager(Manager):
    def get_queryset(self):
        return TableChangesLogQueryset(self.model, using=self._db)