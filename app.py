
"""
BLUE (Warehousing System) App
Created on date: 1403/06/20

View source code on GitHub: https://github.com/Mhadi-1382/blue-warehousing-system/
"""

from flask import Flask, render_template, redirect, flash, request, url_for, session
from persiantools.jdatetime import JalaliDateTime
import os

from extensions.config import mySQL


app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("pages/404.html", e=request.path)

@app.route("/", methods=["GET"])
def panel():
    curReadProducts = mySQL.cursor()
    curReadProducts.execute("SELECT * FROM productsPhrchase")
    curSumProducts = mySQL.cursor()
    curSumProducts.execute("SELECT * FROM productsPhrchase")
    sumTotalList = []
    for i in curSumProducts.fetchall():
        sumTotalList.append(int(i[5]))

    curReadProductsSale = mySQL.cursor()
    curReadProductsSale.execute("SELECT * FROM productsSale")
    curSumProductsSale = mySQL.cursor()
    curSumProductsSale.execute("SELECT * FROM productsSale")
    sumTotalListSale = []
    for i in curSumProductsSale.fetchall():
        sumTotalListSale.append(int(i[5]))

    return render_template("index.html", curReadProducts=curReadProducts.fetchall(), sumTotalPrice=sumTotalList, curReadProductsSale=curReadProductsSale.fetchall(), sumTotalPriceSale=sumTotalListSale)

@app.route("/signin/", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        cur = mySQL.cursor()
        cur_ = mySQL.cursor()
        if cur.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password,)) and (email, password):
            cur.execute("SELECT username FROM users WHERE email = %s AND password = %s", (email, password,))
            cur_.execute("SELECT tel FROM users WHERE email = %s AND password = %s", (email, password,))

            session["username"] = cur.fetchone()[0]
            session["email"] = email
            session["tel"] = cur_.fetchone()[0]
            session["password"] = password
            session.permanent = True

            flash(f"{session['username']}، شما با موفقیت وارد پنل شدید.", category="info")

            return redirect(url_for("panel"))
        elif email == "" or password == "":
            flash("لطفا فیلد خالی را پر کنید.", category="warning")
        else:
            flash("خطا! لطفا اطلاعات خود را بررسی کنید.", category="error")
    
    return render_template("pages/signin.html")
@app.route("/signout/", methods=["GET"])
def sign_out():
    session.clear()

    return redirect(url_for("sign_in"))

@app.route("/products/", methods=["GET"])
def products():
    curReadProductsPhrchase = mySQL.cursor()
    curReadProductsPhrchase.execute("SELECT * FROM productsPhrchase")
    curReadProductsSale = mySQL.cursor()
    curReadProductsSale.execute("SELECT * FROM productsSale")

    return render_template("panel/products/products.html", curReadProductsPhrchase=curReadProductsPhrchase.fetchall(), curReadProductsSale=curReadProductsSale.fetchall())
@app.route("/products/add/", methods=["GET", "POST"])
def products_add():
    curReadProducts = mySQL.cursor()
    curReadProducts.execute("SELECT * FROM productsPhrchase")
    
    curReadProductsCategory = mySQL.cursor()
    curReadProductsCategory.execute("SELECT DISTINCT productCategory FROM productsPhrchase")

    productDate = str(JalaliDateTime.now().strftime("%Y/%m/%d %H:%M"))
    
    if request.method == "POST":
        productName = request.form.get("productName")
        productNumber = request.form.get("productNumber")
        productCategory = request.form.get("productCategory")
        productPurchasePrice = request.form.get("productPurchasePrice")
        productTotalPrice = request.form.get("productTotalPrice")
        productDiscount = request.form.get("productDiscount")
        productDescription = request.form.get("productDescription")

        cur = mySQL.cursor()
        if cur.execute("INSERT INTO productsPhrchase (productName, productNumber, productCategory, productPurchasePrice, productTotalPrice, productDiscount, productDescription, productDate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (productName, productNumber, productCategory, productPurchasePrice, productTotalPrice, productDiscount, productDescription, productDate,)):
            mySQL.commit()
            cur.close()

            return redirect(url_for("products"))
    
    return render_template("panel/products/add.html", curReadProducts=curReadProducts.fetchall(), curReadProductsCategory=curReadProductsCategory.fetchall(), dateNow=productDate)
@app.route("/products/remove/<int:id>/", methods=["GET"])
def products_remove(id):
    if session["username"] or session["email"] or session["password"]:
        pass
    else:
        return redirect(url_for("signin"))

    curReadProducts = mySQL.cursor()
    if curReadProducts.execute(f"SELECT * FROM productsPhrchase WHERE productId = {id}"):
        curRemoveProduct = mySQL.cursor()
        curRemoveProduct.execute(f"DELETE FROM productsPhrchase WHERE productId = '{id}'")
        mySQL.commit()
        curRemoveProduct.close()
        
        return redirect(url_for("products"))
    else:
        return redirect(url_for("products")), flash("حذف محصول با مشکل مواجه شده است.", category="error")
@app.route("/products/edit/<int:id>/", methods=["GET", "POST"])
def products_edit(id):
    if session["username"] or session["email"] or session["password"]:
        pass
    else:
        return redirect(url_for("signin"))

    curReadProducts = mySQL.cursor()
    if curReadProducts.execute(f"SELECT * FROM productsPhrchase WHERE productId = {id}"):
        if request.method == "POST":
            productName = request.form.get("productName")
            productNumber = request.form.get("productNumber")
            productCategory = request.form.get("productCategory")
            productPurchasePrice = request.form.get("productPurchasePrice")
            productTotalPrice = request.form.get("productTotalPrice")
            productDiscount = request.form.get("productDiscount")
            productDescription = request.form.get("productDescription")
            productDate = str(JalaliDateTime.now().strftime("%Y/%m/%d %H:%M"))

            curEditProduct = mySQL.cursor()
            if curEditProduct.execute(f"UPDATE productsPhrchase SET productName = '{productName}', productNumber = '{productNumber}', productCategory = '{productCategory}', productPurchasePrice = '{productPurchasePrice}', productTotalPrice = '{productTotalPrice}', productDiscount = '{productDiscount}', productDescription = '{productDescription}', productDate = '{productDate}' WHERE productId = '{id}'"):
                mySQL.commit()
                curEditProduct.close()

                return redirect(url_for("products"))
    else:
        return redirect(url_for("products")), flash("ویرایش محصول با مشکل مواجه شده است.", category="error")

    return render_template("panel/products/update_phrchase.html", curReadProducts=curReadProducts.fetchall())
@app.route("/products/search/", methods=["GET", "POST"])
def products_search():
    if session["username"] or session["email"] or session["password"]:
        pass
    else:
        return redirect(url_for("signin"))

    productSearch = request.form.get("productSearch")
    
    curSearchProducts = mySQL.cursor()
    curSearchProducts.execute("SELECT * FROM productsPhrchase WHERE productName LIKE '%{}%'".format(productSearch))

    return render_template("panel/products/search_phrchase.html", productSearchResult=productSearch, searching=curSearchProducts.fetchall())
@app.route("/products/sale/add/", methods=["GET", "POST"])
def products_sale_add():
    if session["username"] or session["email"] or session["password"]:
        pass
    else:
        return redirect(url_for("signin"))

    if request.method == "POST":
        productTotalNumber = int(request.form.get("productTotalNumber"))
        productSeries = request.form.get("productSeries")
        productName = request.form.get("productName")
        productNumber = int(request.form.get("productNumber"))
        productPrice = request.form.get("productPrice")
        productTotalPrice = request.form.get("productTotalPrice")
        productDate = str(JalaliDateTime.now().strftime("%Y/%m/%d %H:%M"))
        productNumberCalc = productNumber - productTotalNumber

        curWriteProductSale = mySQL.cursor()
        if curWriteProductSale.execute("INSERT INTO productsSale (productSeries, productName, productNumber, productPrice, productTotalPrice, productDate) VALUES (%s,%s,%s,%s,%s,%s)", (productSeries, productName, productNumber, productPrice, productTotalPrice, productDate,)):
            curEditProductPhrchase = mySQL.cursor()
            curEditProductPhrchase.execute(f"UPDATE productsPhrchase SET productNumber = '{str(productNumberCalc)[1::]}' WHERE productId = '{productSeries}'")
            mySQL.commit()

            curEditProductPhrchase.close()
            curWriteProductSale.close()

            return redirect(url_for("products_add")), flash(f"محصول ({productName}) با موفقیت برای فروش ثبت شد.", category="success")
        else:
            return redirect(url_for("products_add")), flash(f"محصول ({productName}) برای فروش با مشکل مواجه شد.", category="error")
@app.route("/products/sale/remove/<int:id>/", methods=["GET"])
def products_sale_remove(id):
    if session["username"] or session["email"] or session["password"]:
        pass
    else:
        return redirect(url_for("signin"))

    curReadProductsSale = mySQL.cursor()
    if curReadProductsSale.execute(f"SELECT * FROM productsSale WHERE productId = {id}"):
        curRemoveProductSale = mySQL.cursor()
        curRemoveProductSale.execute(f"DELETE FROM productsSale WHERE productId = '{id}'")
        mySQL.commit()
        curRemoveProductSale.close()
        
        return redirect(url_for("products"))
    else:
        return redirect(url_for("products")), flash("حذف محصول با مشکل مواجه شده است.", category="error")
@app.route("/products/sale/search/", methods=["GET", "POST"])
def products_sale_search():
    if session["username"] or session["email"] or session["password"]:
        pass
    else:
        return redirect(url_for("signin"))

    productSearch = request.form.get("productSearch")
    
    curSearchProducts = mySQL.cursor()
    curSearchProducts.execute("SELECT * FROM productsSale WHERE productName LIKE '%{}%'".format(productSearch))

    return render_template("panel/products/search_sale.html", productSearchResult=productSearch, searching=curSearchProducts.fetchall())

@app.route("/reports/", methods=["GET"])
def reports():
    curReadProducts = mySQL.cursor()
    curReadProducts.execute("SELECT * FROM productsPhrchase")
    curSumProducts = mySQL.cursor()
    curSumProducts.execute("SELECT * FROM productsPhrchase")
    sumTotalList = []
    for i in curSumProducts.fetchall():
        sumTotalList.append(int(i[5]))

    curReadProductsSale = mySQL.cursor()
    curReadProductsSale.execute("SELECT * FROM productsSale")
    curSumProductsSale = mySQL.cursor()
    curSumProductsSale.execute("SELECT * FROM productsSale")
    sumTotalListSale = []
    for i in curSumProductsSale.fetchall():
        sumTotalListSale.append(int(i[5]))

    return render_template("panel/reports.html", curReadProducts=curReadProducts.fetchall(), sumTotalPrice=sumTotalList, curReadProductsSale=curReadProductsSale.fetchall(), sumTotalPriceSale=sumTotalListSale)

@app.route("/file_manager/", methods=["GET"])
def file_manager():
    curReadProductsPhrchase = mySQL.cursor()
    curReadProductsPhrchase.execute("SELECT * FROM productsPhrchase")
    curReadProductsSale = mySQL.cursor()
    curReadProductsSale.execute("SELECT * FROM productsSale")
    curReadUsers = mySQL.cursor()
    curReadUsers.execute("SELECT * FROM users")

    return render_template("panel/manager/file_manager/file_manager.html", lenProductsPhrchase=int(len(curReadProductsPhrchase.fetchall())), lenProductsSale=int(len(curReadProductsSale.fetchall())), lenUsers=int(len(curReadUsers.fetchall())))
@app.route("/file_manager/products/phrchase/", methods=["GET"])
def file_manager_products_phrchase():
    curReadProducts = mySQL.cursor()
    curReadProducts.execute("SELECT * FROM productsPhrchase")

    return render_template("panel/manager/file_manager/products_phrchase.html", readProducts=curReadProducts.fetchall())
@app.route("/file_manager/products/sale/", methods=["GET"])
def file_manager_products_sale():
    curReadProducts = mySQL.cursor()
    curReadProducts.execute("SELECT * FROM productsSale")

    return render_template("panel/manager/file_manager/products_sale.html", readProducts=curReadProducts.fetchall())
@app.route("/file_manager/users/", methods=["GET"])
def file_manager_users():
    curReadUsers = mySQL.cursor()
    curReadUsers.execute("SELECT * FROM users")

    return render_template("panel/manager/file_manager/users.html", readUsers=curReadUsers.fetchall())
@app.route("/user_manager/", methods=["GET"])
def user_manager():
    curReadUsers = mySQL.cursor()
    curReadUsers.execute("SELECT * FROM users")

    return render_template("panel/manager/user_manager.html", curReadUsers=curReadUsers.fetchall())
@app.route("/user_manager/add/", methods=["GET", "POST"])
def user_manager_add():
    if session["username"] or session["email"] or session["password"]:
        pass
    else:
        return redirect(url_for("signin"))

    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        tel = request.form.get("tel")
        password = request.form.get("password")
        date = str(JalaliDateTime.now().strftime("%Y/%m/%d %H:%M"))

        curAddUserManager = mySQL.cursor()
        if curAddUserManager.execute("INSERT INTO users (username, email, tel, password, date) VALUES (%s,%s,%s,%s,%s)", (username, email, tel, password, date,)):
            mySQL.commit()
            curAddUserManager.close()

            return redirect(url_for("user_manager"))
@app.route("/user_manager/remove/<int:id>/", methods=["GET"])
def user_manager_remove(id):
    if session["username"] or session["email"] or session["password"]:
        pass
    else:
        return redirect(url_for("signin"))

    curReadUserManager = mySQL.cursor()
    if curReadUserManager.execute(f"SELECT * FROM users WHERE id = {id}"):
        curRemoveUserManager = mySQL.cursor()
        curRemoveUserManager.execute(f"DELETE FROM users WHERE id = '{id}'")
        mySQL.commit()
        curRemoveUserManager.close()
        
        return redirect(url_for("user_manager"))
    else:
        return redirect(url_for("user_manager")), flash("حذف کاربر با مشکل مواجه شده است.", category="error")
@app.route("/user_manager/edit/<int:id>/", methods=["GET", "POST"])
def user_manager_edit(id):
    if session["username"] or session["email"] or session["password"]:
        pass
    else:
        return redirect(url_for("signin"))

    curReadUserManager = mySQL.cursor()
    if curReadUserManager.execute(f"SELECT * FROM users WHERE id = {id}"):
        if request.method == "POST":
            username = request.form.get("username")
            email = request.form.get("email")
            tel = request.form.get("tel")
            password = request.form.get("password")

            curEditUserManager = mySQL.cursor()
            if curEditUserManager.execute(f"UPDATE users SET username = '{username}', email = '{email}', tel = '{tel}', password = '{password}' WHERE id = '{id}'"):
                mySQL.commit()
                curEditUserManager.close()

                return redirect(url_for("user_manager"))
    else:
        return redirect(url_for("user_manager")), flash("ویرایش کاربر با مشکل مواجه شده است.", category="error")

@app.route("/settings/", methods=["GET"])
def settings():
    if session["username"] or session["email"] or session["password"]:
        pass
    else:
        return redirect(url_for("signin"))

    curReadSettings = mySQL.cursor()
    curReadSettings.execute(f"SELECT * FROM users WHERE username = '{session['username']}' AND email = '{session['email']}' AND password = '{session['password']}'")

    return render_template("panel/settings/settings.html", curReadSettings=curReadSettings.fetchall())
@app.route("/settings/edit_account/<int:id>/", methods=["GET", "POST"])
def settings_edit_account(id):
    if session["username"] or session["email"] or session["password"]:
        pass
    else:
        return redirect(url_for("signin"))
    
    if request.method == "POST":
        curReadSettings = mySQL.cursor()
        if curReadSettings.execute(f"SELECT * FROM users WHERE id = {id}"):
            if request.method == "POST":
                username = request.form.get("username")
                email = request.form.get("email")
                tel = request.form.get("tel")
                password = request.form.get("password")

                curEditSettings = mySQL.cursor()
                if curEditSettings.execute(f"UPDATE users SET username = '{username}', email = '{email}', tel = '{tel}', password = '{password}' WHERE id = '{id}'"):
                    mySQL.commit()
                    curEditSettings.close()

                    session.clear()

                    return redirect(url_for("settings")), flash("تغییرات با موفقیت اعمال شد.", category="success")


if __name__ == "__main__":
    app.run(debug=True)
