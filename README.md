Name: Muhammad Arsyad Avmeilputra
NPM: 2506556246


### Assignment 1

-Did not use AI

1.My portfolio website design mainly uses the <section> element. I used it to differentiate (currently) 3 parts/section of the website, which are Profile, Skills, and Projects. The usage of this element provided me clear boundaries for each sections of the website. It allowed me to focus develop one section or the other without mixing up the codes between section.


2. Initially, I started designing the web without applying the responsive concept. By using the basic unit of 'px' to change the width and height of elements, I was able to arrange the structure based on my design objective. However, majority of the structure falls apart when I then minimize the browser. That is when I realised the model of that current code doesn't provide good page view in other devices and started to try apply the responsive concept. 

Two of the challenges I faced was trying to change a horizontal element structure into a vertical structure when the width of the page view is minimized and also trying to make contents to not get covered by the minimized view. The changes mainly focused on elements that is very long or creates a long sequence, while other elements with short lengths such as titles can still fit well without major changes. It took quite a long time and many trials and errors to finally attain a satisfiable responsive design. (Still, perhaps it can be further improve)


3. Based on my understanding, one of the limitations of a static web is the large number of updates or modifying codes to reach of specific goal when designing the web. While in a dynamic web, it is able to connect with a database and through some process, we can update the web only through an administrative interface, without needing to change the codes manually. 



### Assignment 2

-Used AI only try resolve a problem when adding data through Django shell. Other than that part, did not used AI.

1. When a user opens the portfolio web page, a request is sent through the internet and then received by Django. From Django, the request will be forwarded to View by URLs. The role of View is to retrieve and process data from the model data based on incoming requests. Model data describes the data that will be used. After retrieving the data, View will pass it to Template. The Template which is an HTML file acts as the viewing page. It will be rendered by Django and the user will able to see the web page as the response.

The difference between the URLs of an application and a project is that the application's URLs connects to a View to allow page viewing and switching, while the project's URLs connects to an application (or more).


2. In this case, the data has the same format. For example, in the Experience page, the data has a category, title, description, and status. Since for every experience the format is the same, writing large amount of data straight to the template would cause the code to be messy. Storing data in a model prevents redundancy in the template. It keeps the template clean while still being able to modify or add new data.


3. When applying change to the Model file, 'makemigrations' creates the migration files. It acknowledges the changes that happened to the Model. As for 'migrate' it applies the changes to the database. Without the 'migrate' command, it only knows what are the changes but does not implement it. An example is adding a new page such as Project. In the Model, we create a Project class with its descriptions (id, title, description, etc.). To apply this new change, we run both 'makemigrations' and 'migrate' commands. 


### Assignment 3

1. Django’s ModelForm makes the developing process for forms more convinient. It has its own file which is 'forms.py' that allows developer to focus more when writing form codes (seperated form the HTML file) and reduces code redundancy. It also handles backend validation, where it automatically catches an error when user inputs a wrong input type to a field.

The {% csrf_token %} is a security measure for any form with POST requests. It generates a unique token/code. When a form is submitted, Django checks this token to guarantee that the data is actually coming from the user's website, not a malicious third-party script.

2. There are several reasons. First, JSON is easier to read since it is cleaner compared to XML that has a dense tree structure. Second, it is lighter in size because it uses simple key-value pairs. Lastly, it integrates smoothly with JavaScript without needing further conversion process, where JavaScript has been relied heavily in nowadays web development.

3. Flow:
    1) The browser requests a specific URL.
    2) Django's urls.py routes the request to the correct view function.
    3) The view queries the database using the Django ORM.
    4) The view serializes that database query into a JSON format.
    5) The view wraps the JSON in an HttpResponse and sends it back over the internet to the browser.

The reason serialization process is required because it acts as a translation step. It removes all the complex Python logic and converts the raw data (which are Python objects received from querying the database) into a standard text (JSON) that any system can receive and understand.