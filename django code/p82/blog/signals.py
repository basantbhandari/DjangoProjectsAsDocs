from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, post_init, pre_save, post_save, pre_delete, post_delete, pre_migrate, post_migrate
from django.core.signals import request_started, request_finished, got_request_exception
from django.db.backends.signals import connection_created


@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print("************************************")
    print("Logged-in Signal....................")
    print("sender: ", sender)
    print("request: ", request)
    print("user: ", user)
    print("password: ", user.password)
    print(f'kwargs:  {kwargs}')


# user_logged_in.connect(login_success, sender=User)


@receiver(user_logged_out, sender=User)
def logout_success(sender, request, user, **kwargs):
    print("************************************")
    print("Logged-out Signal....................")
    print("sender: ", sender)
    print("request: ", request)
    print("user: ", user)
    print("password: ", user.password)
    print(f'kwargs:  {kwargs}')


# user_logged_out.connect(logout_success, sender=User)


@receiver(user_login_failed)
def login_failed(sender, credentials, request, **kwargs):
    print("************************************")
    print("Logged-in failed Signal....................")
    print("sender: ", sender)
    print("request: ", credentials)
    print("user: ", request)
    print(f'kwargs:  {kwargs}')


# user_login_failed.connect(login_failed, sender=User)


@receiver(pre_save, sender=User)
def at_beginning_save(sender, instance, **kwargs):
    print("************************************")
    print("Pre save Signal....................")
    print("sender: ", sender)
    print("instance: ", instance)
    print(f'kwargs:  {kwargs}')


# pre_save.connect(at_beginning_save, sender=User)


@receiver(post_save, sender=User)
def at_last_save(sender, instance, created, **kwargs):
    if created:
        print("************************************")
        print("Post save Signal....................")
        print("Created....................")
        print("sender: ", sender)
        print("instance: ", instance)
        print("Created: ", created)
        print(f'kwargs:  {kwargs}')

    else:
        print("************************************")
        print("Post save Signal....................")
        print("Updated....................")
        print("sender: ", sender)
        print("instance: ", instance)
        print("Created: ", created)
        print(f'kwargs:  {kwargs}')


# post_save.connect(at_last_save, sender=User)


@receiver(pre_delete, sender=User)
def at_beginning_delete(sender, instance, **kwargs):
    print("************************************")
    print("Pre delete Signal....................")
    print("sender: ", sender)
    print("instance: ", instance)
    print(f'kwargs:  {kwargs}')


# pre_delete.connect(at_beginning_delete, sender=User)


@receiver(post_delete, sender=User)
def at_last_delete(sender, instance, **kwargs):
    print("************************************")
    print("Post deleted Signal....................")
    print("Deleted....................")
    print("sender: ", sender)
    print("instance: ", instance)
    print(f'kwargs:  {kwargs}')


# post_delete.connect(at_last_delete, sender=User)


@receiver(pre_init, sender=User)
def at_beginning_init(sender, *args, **kwargs):
    print("************************************")
    print("Pre init Signal....................")
    print("sender: ", sender)
    print(f'args:  {args}')
    print(f'kwargs:  {kwargs}')


# pre_init.connect(at_beginning_init, sender=User)


@receiver(post_init, sender=User)
def at_last_init(sender, *args, **kwargs):
    print("************************************")
    print("Post init Signal....................")
    print("sender: ", sender)
    print(f'args:  {args}')
    print(f'kwargs:  {kwargs}')


# post_init.connect(at_last_init, sender=User)


@receiver(request_started)
def at_beginning_request(sender, environ, **kwargs):
    print("************************************")
    print("Requested get started Signal....................")
    print("sender: ", sender)
    print('environ : ', environ)
    print(f'kwargs:  {kwargs}')


# request_started.connect(at_beginning_request, sender=User)


@receiver(request_finished)
def at_last_request(sender, **kwargs):
    print("************************************")
    print("Request Finished Signal....................")
    print("sender: ", sender)
    print(f'kwargs:  {kwargs}')


# request_finished.connect(at_last_request, sender=User)


@receiver(got_request_exception)
def at_exception_request(sender, request, **kwargs):
    print("************************************")
    print("Request exception Signal....................")
    print("sender: ", sender)
    print('request : ', request)
    print(f'kwargs:  {kwargs}')


# got_request_exception.connect(at_exception_request, sender=User)


@receiver(pre_migrate)
def before_install_app(sender, app_config, verbosity, interactive, using, plan,
                       apps, **kwargs):
    print("************************************")
    print("Before Install app....................")
    print("sender: ", sender)
    print("sender: ", app_config)
    print("sender: ", verbosity)
    print("sender: ", interactive)
    print("sender: ", using)
    print("sender: ", interactive)
    print("sender: ", plan)
    print("sender: ", apps)
    print(f'kwargs:  {kwargs}')


# pre_migrate.connect(before_install_app)


@receiver(post_migrate)
def at_end_migrate_install_app(sender, app_config, verbosity, interactive,
                               using, plan, apps, **kwargs):
    print("************************************")
    print("Before Install app....................")
    print("sender: ", sender)
    print("sender: ", app_config)
    print("sender: ", verbosity)
    print("sender: ", interactive)
    print("sender: ", using)
    print("sender: ", interactive)
    print("sender: ", plan)
    print("sender: ", apps)
    print(f'kwargs:  {kwargs}')


# post_migrate.connect(at_end_migrate_install_app)


@receiver(connection_created)
def conn_db(sender, connection, **kwargs):
    print("****************************************************************")
    print(".................Initial connection to the database............")
    print("****************************************************************")
    print("sender:", sender)
    print("connection:", connection)
    print(f'kwargs:  {kwargs}')


# connection_created.connect(conn_db)
