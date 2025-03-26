import functools
import time
#ثبت ورودی و خروجی توابع
def log_execution(func) :
    functools.wraps(func)
    def wrapper(*args,**kwargs):
        print(f"اجرای تابع: {func.__name__} | ورودی‌ها: {args} {kwargs}")
        result= func( *args , **kwargs)
        print(f'خروجی: {result}')
        return result
    return wrapper
#سطح دسترسی
def admin(func):
    functools.wraps(func)
    def wrapper(*args, **kwargs):
        user=kwargs.get('role','user')
        if user !='admin'.lower():
            print('دسترسی غیر مجاز ')
            return None
        else:
            return func(*args, **kwargs)
    return wrapper

#کش کردن خروجی توابع
@functools.lru_cache(maxsize=5)
@log_execution
def get_user_data(user_id):
    print("دریافت اطلاعات از دیتابیس....")
    time.sleep(2)
    return {"id": user_id, "name": f"User{user_id}"}


#تنظیم مقدار پیش فرض برای ارسال پیام
send_notification=functools.partial(print,'پیام:')

#بررسی زمان اجرای توابع
def time_execution(func):
    functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time=time.time()
        result=func(*args, **kwargs)
        end_time=time.time()
        print(f" زمان اجرا: {end_time - start_time:.3f} ثانیه")
        return result
    return wrapper
#-----------------------------------------------------------------
#main

#ثبت کاربر
@log_execution
def register_user(username):
    print(f'{username} کاربر ثبت شد')
    return {"username": username, "status": "registered"}

#حذف کاربر
@admin
@log_execution
def delete_user(username, role='user'):
    print(f" کاربر {username} حذف شد!")
    return {"username": username, "status": "deleted"}


#بررسی زمان
@time_execution
def process():
    print('درحال پردازش....')
    time.sleep(3)
    return 'پردازش تمام شد'


# اجرای تستی پروژه
register_user("ali")
register_user("reza")

get_user_data(1)
get_user_data(1)  # از کش خوانده می‌شود

send_notification("سیستم به‌روز شد!")

delete_user("reza", role="user")
delete_user("reza", role="admin")

process()


