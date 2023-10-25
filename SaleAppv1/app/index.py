from flask import Flask, render_template, request
import dao
app = Flask(__name__)

@app.route("/")
def index():
    kw = request.args.get('kw')
    cate = dao.load_categories()
    products = dao.load_products(kw=kw)
    return render_template("index.html", categories=cate, products=products)


if __name__ == "__main__":
    app.run(debug=True)