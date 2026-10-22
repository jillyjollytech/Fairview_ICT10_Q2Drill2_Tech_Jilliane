from pyscript import document, display

def addmember(e):

    G7 = {'Ayano Aishi', 'Amai Odayaka', 'Shoku Tsuburaya'}
    G8 = {'Kenko Sukoyaka', 'Seiyo Akanishi', 'Ajia Ashitomi'}
    G9 = {'Saki Miyu', 'Akifumi Anno', 'Banri Masayuki'}
    G10 = {'Jilliane Tech', 'Chikao Tsurumak', 'TJ Sales', 'Aika Iseri'}

    allgrades = G7 | G8 | G9 | G10

    a = document.getElementById("fname").value
    b = document.getElementById("lname").value 

    c = str.upper(a)
    d = str.upper(b)

    document.getElementById("output").innerHTML = "" 
   
    addedmember = (c + " " + d)
    allgrades.add(addedmember)
    members = "<br>".join(sorted(allgrades))
    numberofmembers = len(allgrades)

    e = f"ALL MEMBERS:<br><br>{members}<br><br>"
    document.getElementById("output").innerHTML = e


    f = f"TOTAL NUMBER OF MEMBERS: {numberofmembers}"
    display(f, target = "output")

    #new livelink maam :) -- https://jillyjollytech.github.io/Fairview_ICT10_Q2Drill2_Tech_Jilliane/
