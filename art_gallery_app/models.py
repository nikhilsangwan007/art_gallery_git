from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DbArtist(models.Model):
    artist_id = models.IntegerField(primary_key=True)
    artist_name = models.TextField()
    date_of_birth = models.DateField()
    birthplace = models.TextField()
    art_type = models.TextField()

    class Meta:
        managed = False
        db_table = 'db_artist'


class DbExhibition(models.Model):
    exhibition_id = models.IntegerField(primary_key=True)
    exhibition_name = models.TextField()
    gallery = models.ForeignKey('DbGallery', models.DO_NOTHING)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'db_exhibition'


class DbExhibitionPainting(models.Model):
    painting = models.OneToOneField('DbPainting', models.DO_NOTHING, primary_key=True)
    exhibition = models.ForeignKey(DbExhibition, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'db_exhibition_painting'
        unique_together = (('painting', 'exhibition'),)


class DbGallery(models.Model):
    gallery_id = models.IntegerField(primary_key=True)
    gallery_name = models.TextField()
    location = models.TextField()

    class Meta:
        managed = False
        db_table = 'db_gallery'


class DbPainting(models.Model):
    painting_id = models.IntegerField(primary_key=True)
    artist = models.ForeignKey(DbArtist, models.DO_NOTHING)
    painting_name = models.TextField()
    genre = models.TextField()
    year_of_publish = models.IntegerField()
    price = models.IntegerField()
    rating = models.DecimalField(max_digits=65535, decimal_places=65535)
    painting_url = models.TextField()
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'db_painting'


class DbQueries(models.Model):
    id = models.IntegerField(primary_key=True)
    query = models.TextField()

    class Meta:
        managed = False
        db_table = 'db_queries'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
