from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/pay', methods=['GET', 'POST'])
def pay():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        amount = request.form['amount']

        return render_template(
            'success.html',
            message=f"Payment successful! ₹{amount} received from {name}."
        )

    return render_template('pay.html')


@app.route('/payment-callback')
def payment_callback():

    status = request.args.get('status', 'SUCCESS')

    if status == 'SUCCESS':
        return render_template(
            'success.html',
            message='Paytm payment successful!'
        )

    return render_template(
        'failure.html',
        message='Paytm payment failed!'
    )


@app.route('/food-payment', methods=['GET', 'POST'])
def food_payment():

    if request.method == 'POST':

        dish = request.form['dish']
        price = request.form['price']

        return render_template(
            'success.html',
            message=f"Food payment successful! {dish} - ₹{price}"
        )

    return render_template('food.html')


@app.route('/paypal-payment')
def paypal_payment():

    return render_template(
        'success.html',
        message='PayPal sandbox payment successful!'
    )


if __name__ == '__main__':
    app.run(debug=True)