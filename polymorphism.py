class PaymentMethod:

    def payment_method(self):
        print("Payment is happening")


class Esewa(PaymentMethod):

    def payment_method(self):
        print("Payment is processing using Esewa")


payment=PaymentMethod()
esewa=Esewa()

payment.payment_method()
esewa.payment_method()

