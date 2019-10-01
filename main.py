
# Introductory Notes 
 
from flask import Flask, request, redirect, render_template

# Create app variable and set to the
# name of the module in Flask
app = Flask(__name__)

fields = []

@app.route('/')
@app.route('/blog', methods=['POST', 'GET'])
def blog_posts():

   if request.method == 'POST':
      title = request.form['title']
      body = request.form['body']

      fields.append(title, body)

   return render_template('blog_posts.html', title="Add New Posts", fields=fields)

# This is the main file to run the app
# Run Flask in developer mode
if __name__ == '__main__':
   app.run(debug=True)

