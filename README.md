# 636WebAppFinal--- Library Project Report

## Project Structure
The web app contains two seperate interfaces, public and staff.

### Public Interfaces Structure and functions:
![projectStructure](https://user-images.githubusercontent.com/123611954/217092240-4d938ecb-139d-4fd2-9592-a5cff45fab82.jpg)

**Home("/")**
* Search box.   
![image](https://user-images.githubusercontent.com/123611954/217094178-132a17da-1916-4a38-b33d-860d493cf9f9.png)  
-- Allowing users search bookcopy by typing book "title" or/and "author".   
-- "Reset Search" button for user back to default result.

* Book copy availability   
-- Default result rendering all the available book copies with their "loan status", "due date"(if it is on loan) and if it is available to borrow.   
-- Result dynamically change with the search filter.   

* Jump to booklist   
![image](https://user-images.githubusercontent.com/123611954/217096555-31b21dda-dbd7-4746-98b3-b88c0d02436c.png)   

**Books("/listbooks")**    
* Available books   
-- Render all the books in the library with detail.   
-- A bootstrap collapse button displays book description.   
![image](https://user-images.githubusercontent.com/123611954/217097543-b5dee8a7-a8a3-4f8b-b490-c00e81a27460.png)   

### Staff Interfaces Structure and functions:   
![projectStructure (2)](https://user-images.githubusercontent.com/123611954/217116491-ecbf7d00-3153-46d6-a311-4c2d3ad538df.jpg)      

**Home("/staff")**   
* Search box(same as public )   
* Book copy availability    
* Jump to borrower list    
![image](https://user-images.githubusercontent.com/123611954/217116968-2e11ef9a-a5df-472f-b100-6514b4ca7591.png)

**Borrowers("/staff/listborrowers")**    
* Search Box   
-- Allowing staff search borrower by typing borrower "id" or/and "name".   
-- "Reset Search" button for staff back to default result.  
![image](https://user-images.githubusercontent.com/123611954/217120562-3c41d501-f8cb-4b45-9ffc-c137e0e77b2f.png)  

* Add a borrower/ Edit a borrower  
-- Staff click "add borrower" button, a popup modal showed with a post form.   
-- Staff click  "Edit" icon, a popup modal showed with existing data in a post form.   
![projectStructure (4)](https://user-images.githubusercontent.com/123611954/217122612-1b5003db-363a-475d-ae79-012a244471b2.jpg)    

* Borrower detail list    
-- Render a list of borrower with full detail     

**Current Loan("/staff/bookreturn")**    
* Render a list of current loan   
-- Each record comes with a return button    

* Return a loan   
-- staff click the "Return" button, a popup alert showed up, ask the staff to confirm the operation, if confirmed, the bookcopy will be returned.   

* Add Loan   
-- staff click the "Add Loan" button, a popup select form displayed, a loan can be added with borrower and available book copy.   

![projectStructure (5)](https://user-images.githubusercontent.com/123611954/217133326-6df06dbc-201c-4aed-a9fb-5168efd4f2ef.jpg)

**Loan Report("/staff/overduereport")**    
-- Default page of loan reports.   
-- Providing a side bar nav for three loan report pages.   

**Overdue Report("/staff/overduereport")**    
* Render overdue book and it's borrower , borrower's name only showed once

**Loan Summary("/staff/loansummary")**   
* Render  books and their loaned times.

**Borrower Summary("/staff/borrowersummary")**   
* Render borrowers and their loan counts.  

## Assumptions and design Decisions   

### Search box on book copy availability page  

* The placement of search box     
  The search box could be created as an individual page or on the same page of search result. Considering, if there is only a single search box on home page(such as     Google), the space would be wasted and also there will be another page called "Available Books". To help public users get the relevant information straight forward,   the search box is placed on the top of available book copy list. When a search requested, the list is filtered.
  
* "POST" or "GET" ?    
  It is always a disscussion when it comes to "search" function. POST is a better practice to prevent SQL injection from URL bar and dealing with complex search. However   in this case, it is more appropriate to use "GET" as the user would like to see what they have searched with URL changing. With the help of "GET" method, the result   can be rendered with flexibility and less errors. A SQL binding has been done with python to protect database from injection.
  
* Search result    
  Whether the search result should be the searched book or book copy with availability? It is not very clearly discribed in project requirment. From the user point of   view, the book copy availability list is showed. The user needs to know which book is available and its format, rather than just the book details. They can browse     book details in the "books" page. Would be better design if these two pages could be combined as one, so that a user can see its available copy when browse books.

### Route and structure   
* Seperate base.    
  The default base should be used as public interface, therefore, the "staff.html" could be used as a staff system base for its children pages. All the functions and     pages which should be included by staff management system should come with a similar format of route "staff/XXX". It represents this page is part of staff interface,   also would be more secured from public users.   
* "current loan" with book return function.   
  It is a good practice to use same route as its page title. The page showed a list of current loan and offer an "return book" function, to display both its content     and functionality, "Current Loan" is set as page title and "bookreturn" is set as route. There could be a better solution to explore in the future.  
* "Loan report"--- a reports access.   
  There are three different loan reports in the project scope. If each of reeports is rendered with individual access from navigation bar, it is useful but design       would be not ideal. A shared interface has been created for the reports to make the pages more structured.   

### Primary key Id hidden or display?   
* Public interface    
  Absolutely hidden. All sorts of ID should be compeleted hidden from public users for security reason. There is no ID has been included in the public page design.   
* Staff interface  
  It depends on if it is necessary. If the operation is dealing with names or titles, the possible same value would be confusing, it is a good practice to display       IDs to prevent errors. Therefore, if the content is about borrower or book title, an ID is always displayed, such as on borrower page and book return page, as well     as relevant information may trigger operation, such as loan report. My consideration is different from the project requirment. 

### An individual page or a bootstrap modal?   
Bootstrap modals have been used across the web app development. It increased the page interactivity and reduce the data pass between two pages. 

### Error message   
There are different ways to display error message in a web app. Bootstrap offers well structured alert module to display error message. It has been used on "no result" search page . 
![image](https://user-images.githubusercontent.com/123611954/217148668-5ef882d9-83c9-4dd7-a23c-a4833b3336b9.png)   

### Validation  
Validation is appied with bootstrap default function. A more complex validation can be done with JS in the future.   

### The status of "Audio Book" and "eBook"   
"Audio Book" and "eBook" can be loaned regardless of they are "on loan" or "returned", but it is good to tell users that on loaned soft copy is also available. Therefore, the loan status and due date still be showed when it comes to soft copy.

## Discussion to support multiple branches.   

### Modification of Database.    
* Create a "librarybranch" table, "branchid" as primary key has auto increment, "branchname" as column shows branch names.   
![image](https://user-images.githubusercontent.com/123611954/217160766-c7832fab-10d5-4aad-a538-77ad3f824d4d.png)

* Insert "branchid" as foreign key into all the other tables.  
![image](https://user-images.githubusercontent.com/123611954/217161417-4752ddae-7733-40eb-a8d4-3a44d05cf9d3.png)

### Modification of App Development.   
* Public interface   
  On "home" page, showing general welcome information and introduction of Waikirikiri Library. When user searches a book , ask him/her whether they would like to         search in a specific branch all across whole library. If they search across whole library, showing which branch the book belongs in the list. 
* Staff interface   
  A library staff can only access the branch which he/she is working for to manage loans. Add login/authentication would be the best practice to scale app. Another       option would be a differentiated route such as "/staff/chc". Staff would only be able to see and manage the borrowers and loans in that branch.









































