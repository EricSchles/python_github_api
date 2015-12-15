from subprocess import call
import pickle
from glob import glob
import os
import json

def generate_request(endpoint="",output_file="",parameters={},username="EricSchles"):
    """
    endpoint is of the form https://api.github.com/endpoint
    output_file is of the form '.json' all other file extensions will be ignored
    parameters are the standard parameters from the github documentation
    """
    if endpoint == "":
        return "endpoint required"
    if output_file == "":
        return "output file required"

    oauthkey = pickle.load(open("oauthkey.pickle","r"))
    username= username+":"+oauthkey
    request = "curl -o {0} -i -u {1} {2}".format(output_file,username,endpoint)
    parameters["access_token"] = oauthkey
    params = "?"
    for param in parameters.keys():
        params += param + "=" + parameters[param] +"&"
    params = params.rstrip("&")
    request += params
    return request

def clean_json(output_file):
    with open(output_file,"r") as f:
        to_clean = f.read()
    to_clean = to_clean.split("\n")
    final_file = ""
    for line in to_clean:
        if not "\r" in line:
            final_file += line
    with open(output_file,"w") as f:
        f.write(final_file)
    return final_file

def do_request(request):
    call(request.split(" "))
    

def make_request(endpoint="",output_file="",parameters={},username="EricSchles",persistent=True):
    request = generate_request(endpoint=endpoint,output_file=output_file,parameters=parameters,username=username)
    do_request(request)
    clean_json(output_file)
    response = json.load(open(output_file,"r"))
    if not persistent:
        os.remove(output_file)
    return response

def request_for_testing():
    return make_request(
        endpoint="https://api.github.com/user",
        output_file="user.json"
    )

if __name__ == '__main__':
    response = make_request(
        endpoint="https://api.github.com/orgs/department-of-veterans-affairs/members",
        output_file="members.json",
        parameters = {
            "per_page":"200"
        })
    )
    
     
