def get_month_decorator(func):
    def wrapper(month):
        if month < 1 or month > 12:
            raise ValueError("Invalid month value. Please provide a number between 1 and 12 (inclusive).")
        return func(month)
    return wrapper


@get_month_decorator
def get_month(month):
    month_names = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    return month_names[month - 1]
