#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import caesar
import cgi

def build_page(textarea_content):
    heading= "<h2>Enter the text and rotation amount</h2>"

    message_label= "<label>Enter your message:</label>"
    textarea = "<textarea name= 'message'>"+textarea_content +"</textarea>"

    rot_label ="<label>Rotate by:</label>"
    rotation_input = "<input type = 'number' name ='rotation'/>"
    submit = "<input type='submit'/>"

    form = ("<form method ='post'>"+"<b>"+ message_label+"</b>"+textarea+"<br>"+
    "<b>"+rot_label+"</b>"+
    "<br>"+rotation_input+ "<br>"+ submit +"</form>")
    return heading +form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page("")
        self.response.write(content)
    def post(self):
        message =self.request.get('message')
#        escaped_text = cgi.escape(message)
        rotation = int(self.request.get('rotation'))
        encrypted_text = caesar.encrypt(message,rotation)
        escaped_text = cgi.escape(encrypted_text)
        content = build_page(escaped_text)
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
