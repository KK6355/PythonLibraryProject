from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
import re
import datetime
import mysql.connector
from mysql.connector import FieldType
import connect

app = Flask(__name__)

dbconn = None
connection = None

def getCursor():
    global dbconn
    global connection
    connection = mysql.connector.connect(user=connect.dbuser, \
    password=connect.dbpass, host=connect.dbhost, \
    database=connect.dbname, autocommit=True)
    dbconn = connection.cursor()
    return dbconn

@app.route("/")
def home():
    # search function
    title = request.args.get('title')
    author = request.args.get('author')
    # format binding variable
    searchTitle = "%" + str(title) + "%"
    searchAuthor = "%" + str(author)+ "%"
    error_message_noResult = ""
    cur = getCursor()
    # run this SQL if a search requested
    if title or author:
       
        sql=""" SELECT books.booktitle, books.author, bookcopies.format, min(loans.returned), max(loans.loandate) FROM bookcopies 
        INNER JOIN books ON books.bookid = bookcopies.bookid 
         Left JOIN loans ON loans.bookcopyid=bookcopies.bookcopyid
          WHERE books.booktitle LIKE %s AND books.author LIKE %s
        GROUP BY bookcopies.bookcopyid 
        ORDER BY books.booktitle """
        cur.execute(sql, (searchTitle, searchAuthor))
    # render all records as default
    else:
        sql=""" SELECT books.booktitle, books.author, bookcopies.format, min(loans.returned), max(loans.loandate) FROM bookcopies 
        INNER JOIN books ON books.bookid = bookcopies.bookid 
        LEFT JOIN loans ON loans.bookcopyid=bookcopies.bookcopyid
        GROUP BY bookcopies.bookcopyid 
        ORDER BY books.booktitle """
        title=""
        author=""
        cur.execute(sql)
    fetchBooks = cur.fetchall()
    # render error message
    if len(fetchBooks) == 0:
        error_message_noResult = f" Your search --- book title: <{title}>, book author: '{author}' --- has no result, please try again."
    # get a new list of books
    availableBooks = []
    for fetchBook in fetchBooks:
        if fetchBook[4] and fetchBook[3] != 1 and (fetchBook[2] not in ["eBook","Audio Book"]):
            loandate =datetime.datetime.strptime(str(fetchBook[4]), '%Y-%m-%d')
            timeDate_dueDate = loandate + datetime.timedelta(days=28)
            dueDate =  timeDate_dueDate.strftime('%Y-%m-%d')
        else :
            dueDate = ""
        isAvailable = "NO"
        status = ""
        if fetchBook[3] == 1:
            status = "Returned"
        if fetchBook[3] == 0 and (fetchBook[2] not in ["eBook","Audio Book"]):
            status = "On Loaned"
        if fetchBook[2]  in ["eBook","Audio Book"] or fetchBook[3] == 1 or dueDate=="":
            isAvailable = "YES"  
        availableBooks.append((fetchBook[0],fetchBook[1],fetchBook[2],status, dueDate, isAvailable))
  
    return render_template("base.html", availableBooks= availableBooks, title=title, author=author, error_message_noResult=error_message_noResult)

@app.route("/listbooks")
def listbooks():
    cur = getCursor()
    cur.execute("SELECT * FROM books;")
    bookList = cur.fetchall()
    return render_template("booklist.html", booklist = bookList)    


@app.route("/staff")
def staff_index():
     # search function
    title = request.args.get('title')
    author = request.args.get('author')
    # format binding variable
    searchTitle = "%" + str(title) + "%"
    searchAuthor = "%" + str(author)+ "%"
    error_message_noResult = ""
    cur = getCursor()
    # run this SQL if a search requested
    if title or author:
        sql=""" SELECT books.booktitle, books.author, bookcopies.format, min(loans.returned), max(loans.loandate) FROM bookcopies 
        INNER JOIN books ON books.bookid = bookcopies.bookid 
         Left JOIN loans ON loans.bookcopyid=bookcopies.bookcopyid
          WHERE books.booktitle LIKE %s AND books.author LIKE %s
        GROUP BY bookcopies.bookcopyid 
        ORDER BY books.booktitle """
        cur.execute(sql, (searchTitle, searchAuthor))
    # render all records as default
    else:
        sql=""" SELECT books.booktitle, books.author, bookcopies.format, min(loans.returned), max(loans.loandate) FROM bookcopies 
        INNER JOIN books ON books.bookid = bookcopies.bookid 
         Left JOIN loans ON loans.bookcopyid=bookcopies.bookcopyid
        GROUP BY bookcopies.bookcopyid 
        ORDER BY books.booktitle """
        title=""
        author=""
        cur.execute(sql)
    fetchBooks = cur.fetchall()
     # render error message
    if len(fetchBooks) == 0:
        error_message_noResult = f" Your search --- book title: <{title}>, book author: '{author}' --- has no result, please try again."
     # get a new list of books
    availableBooks = []
    for fetchBook in fetchBooks:
        if fetchBook[4] and fetchBook[3] != 1 and (fetchBook[2] not in ["eBook","Audio Book"]):
            loandate =datetime.datetime.strptime(str(fetchBook[4]), '%Y-%m-%d')
            timeDate_dueDate = loandate + datetime.timedelta(days=28)
            dueDate =  timeDate_dueDate.strftime('%Y-%m-%d')
        else :
            dueDate = ""
        isAvailable = "NO"
        status = ""
        if fetchBook[3] == 1:
            status = "Returned"
        if fetchBook[3] == 0 and (fetchBook[2] not in ["eBook","Audio Book"]):
            status = "On Loaned"
        if fetchBook[2]  in ["eBook","Audio Book"] or fetchBook[3] == 1 or dueDate=="":
            isAvailable = "YES"  
        availableBooks.append((fetchBook[0],fetchBook[1],fetchBook[2],status, dueDate, isAvailable))
    return render_template("staff.html", availableBooks= availableBooks, title=title, author=author, error_message_noResult=error_message_noResult)
@app.route("/staff/listborrowers")
def listborrowers():
    cur = getCursor()
    # search function
    id = request.args.get('id')
    name = request.args.get('name')
    # format binding variable
    searchId = "%" + str(id) + "%"
    searchName = "%" + str(name) + "%"
    error_message_noResult = ""
    # run this SQL if a search requested
    if id or name:
        sql="""SELECT * FROM borrowers
         WHERE borrowerid LIKE %s AND concat(firstname, ' ', familyname) LIKE %s  """
        cur.execute(sql, (searchId, searchName))
    # render all records as default
    else:
        sql="SELECT *  FROM borrowers;"
        id=""
        name=""
        cur.execute(sql)
    borrowerList = cur.fetchall()
    # get error message
    if len(borrowerList) == 0:
        error_message_noResult = f" Your search --- card id: <{id}>, borrow name: '{name}' --- has no result, please try again."
    return render_template("borrowerlist.html", borrowerlist = borrowerList, id=id,name=name,error_message_noResult=error_message_noResult)

@app.route("/borrower/edit", methods=["POST"])
def editBorrow():
    # get post fields from modal form
    id = request.form.get("id",type=int)
    firstName = request.form.get("firstName")
    familyName = request.form.get("familyName")
    dateOfBirth = str(request.form.get("dateOfBirth"))
    houseNumber = request.form.get("houseNumber")
    street = request.form.get("street")
    town = request.form.get("town")
    city = request.form.get("city")
    postalCode = request.form.get("postalCode")
    cur=getCursor()
    sql="""UPDATE borrowers SET firstname=%s,familyname=%s,dateofbirth=%s,
    housenumbername=%s,street=%s,town=%s,
    city=%s,postalcode=%s
     WHERE borrowerid = %s """
    cur.execute(sql, (firstName,familyName,dateOfBirth,houseNumber,street,town,city,postalCode,id))
    # when update succeed, redirect to borrower list
    return redirect("/staff/listborrowers")

@app.route("/borrower/add", methods=["POST"])
def addBorrow():
    # get post fields from modal form
    firstName = request.form.get("firstName")
    familyName = request.form.get("familyName")
    dateOfBirth = str(request.form.get("dateOfBirth"))
    houseNumber = request.form.get("houseNumber")
    street = request.form.get("street")
    town = request.form.get("town")
    city = request.form.get("city")
    postalCode = request.form.get("postalCode")
    cur=getCursor()
    cur.execute("INSERT INTO borrowers (firstname, familyname, dateofbirth, housenumbername, street, town, city, postalcode) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) ;",(firstName,familyName,dateOfBirth,houseNumber,street,town,city,postalCode))
    # when update succeed, redirect to borrower list
    return redirect("/staff/listborrowers")



@app.route("/addloan", methods=["POST"])
def addloan():
    # get post fields from modal form
    borrowerid = request.form.get('borrower')
    bookcopyid = request.form.get('book')
    loandate = request.form.get('loandate')
    cur = getCursor()
    cur.execute("INSERT INTO loans (borrowerid, bookcopyid, loandate, returned) VALUES(%s,%s,%s,0);",(borrowerid, bookcopyid, str(loandate),))
     # when update succeed, redirect to current loan list
    return redirect("/staff/bookreturn")



@app.route("/staff/bookreturn")
def bookreturn():
    # pass loan date to add loan form
    todaydate = datetime.datetime.now().date()
    cur = getCursor()
    # render current loan list 
    sql=""" select br.borrowerid, br.firstname, br.familyname,  
                l.borrowerid, l.bookcopyid, l.loandate, l.loanid, l.returned, b.bookid, b.booktitle, b.author, 
                b.category, b.yearofpublication, bc.format 
            from books b
                inner join bookcopies bc on b.bookid = bc.bookid
                    inner join loans l on bc.bookcopyid = l.bookcopyid
                        inner join borrowers br on l.borrowerid = br.borrowerid
                        where l.returned = 0
            order by br.familyname, br.firstname, l.loandate;"""
    cur.execute(sql)
    loanList = cur.fetchall()

# fetch booklist to select options
    sqlbooks = """SELECT * FROM bookcopies
inner join books on books.bookid = bookcopies.bookid
 WHERE bookcopyid not in (SELECT bookcopyid from loans where (returned <> 1 or returned is NULL) )
 OR  (format = 'Audio Book' or format = 'eBook')
 ;"""
    cur.execute( sqlbooks)
    bookList =cur.fetchall()
# fetch borrower list to select options
    cur.execute("SELECT * FROM borrowers;")
    borrowerList = cur.fetchall()
    
   
    return render_template("bookreturn.html", loanlist = loanList,loandate = todaydate,borrowers = borrowerList, books= bookList)

@app.route("/staff/overduereport")
def overduereport():
    cur = getCursor()
    sql = """SELECT  concat(borrowers.firstname,' ',borrowers.familyname) , borrowers.borrowerid, 
             books.booktitle,bookcopies.format,
            loans.loandate FROM borrowers
             INNER JOIN loans on borrowers.borrowerid = loans.borrowerid
                INNER JOIN bookcopies on loans.bookcopyid=bookcopies.bookcopyid
                    INNER JOIN books on bookcopies.bookid = books.bookid
             WHERE loans.returned = 0 
             ORDER BY borrowers.borrowerid
          
    
    """
    cur.execute( sql)
    loanList =cur.fetchall()
    overdueList = []
    date_today =  datetime.datetime.strptime(str(datetime.date.today()), '%Y-%m-%d')
    # get over days

    for loan in loanList:
        if loan[4]:
            loandate =datetime.datetime.strptime(str(loan[4]), '%Y-%m-%d')
            loanDays = (date_today-loandate).days
            overdueDays = loanDays - 35
            if loanDays >= 35:
                overdueList.append((loan[0],loan[1],loan[2],loan[3], overdueDays))

    return render_template("overduereport.html", overdueList=overdueList)

@app.route("/staff/loansummary")
def loansummary():
    # loan record group by bookid to show each book loaned times
    cur = getCursor()
    sql = """SELECT books.booktitle,bookcopies.bookcopyid,bookcopies.format,  
    count(bookcopies.bookcopyid)AS timesborrowed  
    FROM bookcopies 
    INNER JOIN loans ON loans.bookcopyid = bookcopies.bookcopyid 
    INNER JOIN books ON bookcopies.bookid = books.bookid 
    GROUP BY bookcopies.bookcopyid
    ORDER BY books.booktitle, timesborrowed desc 
    """
    cur.execute( sql)
    summaryList =cur.fetchall()
    return render_template("loansummary.html", summaryList=summaryList)

@app.route("/staff/returnBook", methods=["POST"])
def return_book():
    # get post fields from modal alert
    id = request.form.get('id', type=int)
    returned = request.form.get('returned', type=int)
    cur = getCursor()
    cur.execute("UPDATE loans SET returned=%s WHERE loanid=%s ;",(returned,id))
    return redirect("bookreturn")

@app.route("/staff/borrowersummary")
def borrowersummary():
    cur = getCursor()
     # loan record group by borrower id to show each borrower loan times
    sql = """SELECT  concat(borrowers.firstname,' ',borrowers.familyname), borrowers.borrowerid, 
    count(borrowers.borrowerid)AS timesloaned  
    FROM borrowers 
    INNER JOIN loans ON loans.borrowerid = borrowers.borrowerid 
    GROUP BY borrowers.borrowerid 
    ORDER BY timesloaned  desc 
    """
    cur.execute( sql)
    summaryList =cur.fetchall()
    return render_template("borrowersummary.html", summaryList=summaryList)

