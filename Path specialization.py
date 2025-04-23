<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Course specialization page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Course Specialization Portal</h1>
    <p>Welcome to the course specialization page. Here you can find information about various courses and their specializations.</p>
    <p>First of all congratulations on completing the introduction to Software Engineering Module</p>
    <p>Now you can choose a specialization course from the following list:</p>
    <ol type="i">
        <li>Full-stack Web development</li>
        <li>Software Testing</li>
        <li>Mobile App Development</li>
        <li>AI for software engineering</li>
    </ol>
    <img src="https://images.pexels.com/photos/546819/pexels-photo-546819.jpeg?auto=compress&cs=tinysrgb&w=400" alt="image of lines of code" width="300" height="200">
    <p>For more information about the courses, please visit our <a href="https://www.new.com">website</a>.</p>
    <p>You can also reach out the following course moderators</p>
    <table border="3">
        <caption>Course Moderators</caption>
        <thead>
            <tr>
                <th>Course</th>
                <th>Moderator</th>
                <th>Address</th>
                <th>Email</th>
            </tr>
        </thead>
        <tbody>
           
        </thead>
        <tbody>
            <tr>
                <td>Full-stack Web development</td>
                <td>Dr Who</td>
                <td>123 Main St, Cityville</td>
                <td>drwho@gmail.com</td>
            </tr>
            <tr>
                <td>Software Testing</td>
                <td>Dr Tech</td>
                <td>456 Elm St, Townsville</td>
                <td>drtech@gmail.com</td>
            </tr>
            <tr>
                <td>Mobile App Development</td>
                <td>Dr App</td>
                <td>789 Oak St, Villageville</td>
                <td>app@gmail.com</td>
            </tr>
            <tr>
                <td>AI for software engineering</td>
                <td>Dr AI</td>
                <td>101 Pine St, Hamletville</td>
                <td>ai@gmail.com</td>   
            </tr>
        </tbody>
        </table>
        <p>To register online, fill the registration form</p>
        <form action=" register.com" method="post">
            <label for="nme">Name:</label>
            <input type="text" id="nme" name="nme" required placeholder="name"><br>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required placeholder="name@gmail.com"><br>
            <label for="password">Enter a valid password</label>
            <input type="password" id="password" name="password" required pattern="[a-z0-9]{8,}" placeholder="abcd1234"><br>
            <label for="course">Select Course:</label>
            <select id="course" name="course" required>
                <option value="" disabled selected>Select a course</option>
                <option value="fullstack">Full-stack Web development</option>
                <option value="testing">Software Testing</option>
                <option value="mobile">Mobile App Development</option>
                <option value="ai">AI for software engineering</option>
            </select><br>
            <input type="submit" value="Register">
            <fieldset>
                <p>Do you have any previous experience in the selected course?</p>
                <input type="radio" id="yes" name="experience" value="yes">YES
                <input type="radio" id="yes" name="experience" value="no">NO
                <br>
            </fieldset> 
            <fieldset>
                <legend>Any comments</legend>
                <textarea name="comments" rows="4" cols="50" placeholder="Enter your comments here"></textarea><br>
            </fieldset>
            <fieldset></fieldset>
            <label for="terms">I agree to the terms and conditions</label><br>
            <input type="checkbox" id="terms" name="terms" required><br>
            </fieldset>
        </form>



</body>
</html>
