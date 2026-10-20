from pyscript import document, display

def check_candidate_status(e):

 club_members = (
 'Ayano Aishi',
 'Amai Odayaka',
 'Shoku Tsuburaya',
 'Kenko Sukoyaka',
 'Seiyo Akanishi',
 'Ajia Ashitomi',
 'Saki Miyu',
 'TJ Sales'               
) 

 document.getElementById("div2").innerHTML = "" 
 first_name = document.getElementById("fname").value.strip()
 last_name = document.getElementById("lname").value.strip()
 candidate_name = f"{first_name} {last_name}"
 is_member = candidate_name in club_members

 messages = {
     True: f"Congratulations {candidate_name}! You are now part of the Rainbow Catering Club!!",
     False: f"Sorry {candidate_name}, your name is not on the list..."
 }

 result = messages[is_member]
 display(result, target = "div2") 
