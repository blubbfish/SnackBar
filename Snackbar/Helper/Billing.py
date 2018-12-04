from Snackbar.Helper.Database import getcurrbill, get_payment


def rest_bill(userid):
    curr_bill = getcurrbill(userid)
    total_payment = get_payment(userid)
    rest_amount = -curr_bill + total_payment
    return rest_amount