from flask import Flask
from flask_restx import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

# Global user list
users = []

# Sample user list will be carried on
'''
users =
        [
            {"username": "alice", "email_id": "...", "role": "admin"},
            {"username": "bob", "email_id": "...", "role", "editor"}
        ]
'''
# build user parser for query and delete
user_query_parser = reqparse.RequestParser()
user_query_parser.add_argument('user_name', type=str, help="user name to search/delete")

# build the parser for POST which would be JSON body
user_post_parser = reqparse.RequestParser()
user_post_parser.add_argument('user_name', type=str, location='json', help="user name to add as POST Payload")
# we have added totally a new parser here which is not copied from query_parser, hence we are using add_argument instead of replace_argument
user_post_parser.add_argument('email_id', type=str, location='json', help="user email ID")
user_post_parser.add_argument('role', type=str, choices=['admin', 'editor', 'viewer'], location='json', help="user role in the application")

@api.route("/users")
class Findusers(Resource):
    @api.expect(user_query_parser)
    def get(self):
        args = user_query_parser.parse_args()
        if args.user_name:
            match_user = []
            for username_entry in users:
                if args.user_name.lower() in username_entry['username'].lower():
                    match_user.append(username_entry)
            return match_user, 200
        else:
            return users, 200
        #Sample output as a list. It could be set as following GET as well
        '''
        [
            {"username": "alice", "email-id": "..."},
            {"username": "bob", "email-id": "..."}
        ]
        '''
    @api.expect(user_query_parser)
    def delete(self):
        args = user_query_parser.parse_args()
        global users
        new_users = []
        if args.user_name:
            for u in users:
                if u["username"] != args.user_name:
                    new_users.append(u)
            users = new_users
            return "", 204
        else:
            return f"username: {args.user_name} not found"
    @api.expect(user_post_parser)
    def post(self):
        args = user_post_parser.parse_args()
        users.append({
            "username": args.user_name,
            "email": args.email_id,
            "role": args.role
        })
        return {"message": f"user {args.user_name} added!"}, 201
            
            

#Following get is same as above. For practice it is optimized with lit-comprehension
@api.route("/users/list_comph")
class FindUsersLCMH(Resource):
    @api.expect(user_query_parser)
    def get(self):
        args = user_query_parser.parse_args()
        if args.user_name:
            match_filt_usr = [u for u in users if args.user_name.lower() in u["username"].lower()]
            return match_filt_usr, 200
        else:
            return {"users": users}, 200
        #sample output as dictionary like REST API return
        '''
        {
            "users": 
            [
                {"username": "alice", "email-id": "..."},
                {"username": "bob", "email-id": "..."}
            ]
        }
        '''
    @api.expect(user_query_parser)    
    def delete(self):
        args = user_query_parser.parse_args()
        global users
        original_user_count = len(users)
        users = [u for u in users if u["username"] != args.user_name]
        if len(users) < original_user_count:
            return "", 204
        else:
            return {"error": "User not found"}, 404

    @api.expect(user_post_parser)
    def post(self):
        args = user_post_parser.parse_args()
        # Check the duplicate
        if any(u["username"] == args.user_name for u in users):
            return {"message": f"User {args.user_name} already exist"}, 400
        users.append({
            "username": args.user_name,
            "email": args.email_id,
            "role": args.role
        })
        return {"message": f"User {args.user_name} added successfully"}, 201


if __name__ == '__main__':
    app.run(debug=True, port=4999)



