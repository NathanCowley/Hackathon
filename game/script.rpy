#HACKATHON 2023 
#SOLO CREATOR: NATHAN COWLEY
#---------------------------
#PURPOSE: The purpose of this program is to play an informational game
#that not only presents information in a calm fashion, it also instructs them on 
#on how to better 
#-------------------------------


#Beginning of Script


#-----------------------
#Intro Declarations:
# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Sophie!", color = "#FF0044")
define You = Character("You", color = "#0033FF") 
#You Character was meant to be for player interaction.
#---------------------------------------------------------


#UNUSED FUNCTIONALITY: ATTEMPTED TO CONNECT RENPY PROGRAM TO GITHUB TO RECORD PLAYTIME
#GitHub String Fetch
#python: 
#    username = 'NathanCowley'
#    token = 'token'
#    login = requests.get('https://api.github.com/search/repositories?q=github+api', auth=(username,token))



#Game Starts Here.
label start:

#Syntax Notes: 
        #label start: start of program: requires a return
        #show "": -shows a image file from images folder

    #INTRODUCTION TO SOPHIA AND THE GAME!


   
    image main_1 = im.Scale("backg.jpg", 1920, 1080)           #Used for Scaling Down Images
    image puppy = im.Scale("pleasedonthurtme.jpg", 1920, 1080)


    show main_1 #Shows Main Background Image
    show sophia #Shows Sophia Image
    with dissolve    #PERFORMS TRANSITION


    #e "----" command creates text: STOP FORGETTING SECOND SET OF " AT END OF PROGRAM OR IT WONT WORK.

    e "Hello, Everybody!" 
    e "My name is Sophie! I am your guide today on Keeping Yourself Safe on the Internet!"
    e "Today, my creator was tasked with creating a program that represented Personal Wellbeing."
    e "Nathan decided to direct his focus on a crucial issue that he found plaguing many individuals personal wellbeing during and after the COVID pandemic."
    e "That issue is the management and insecurity of personal valuable information and/or data."
    e "So today, Nathan has tasked me with teaching you some tools for protecting yourself while on the internet and thus give you a healthier state of mind."
    e "I will explain my creator's decision at the end, but for now, to make sure all of you are in the right headspace..."
    e "...Lets make sure you are ready! HERES A PICTURE OF A PUPPY TO GET US IN THE MOOD!"

    hide sophia 
    with dissolve

    show puppy
    e ""          #Blank Space for a Delay for Puppy Image
    hide puppy
    show sophia


    #INTRODUCTION TO TOPIC

    e "Some people believe that the best way they can be secure with their internet usage is by creating the tools themselves"
    e "But since we are making the tools digitally, they ACTUALLY would look like..."
    e "01001001 01100110 00100000 01111001 01101111 01110101 00100000 01100011 01100001 01101110 00100000 01110010 01100101 01100001 01100100 00100000 01110100 01101000 01101001 01110011 00101100 00100000 01110111 01100101 01101100 01101100 00100000 01100100 01101111 01101110 01100101 00100001 "
      #YES THIS ACTUALLY MEANS SOMETHING ;)

    e "Sorry, Sorry. Little Computer Science Joke there."
    e "My creator decided the best way to emphasize this was by having this method tought in this visual novel style...a style mostly used for calm, relaxing games that alleviates much pressure and as such take care of your personal wellbeing"
    e "The tools in question today are ones you are most likely familiar with... "
    e "1. Github."
    e "2. A Sandboxed browser."
    e "And 3. A Cloud-Hosted VPN "
    e "Now you might be asking..."
    e "Why do I need to know about these tools? What do these tools have to do with Personal Wellbeing?"
    e "Many projects in this contest may have focused on nutrition and/or physical health. Something that is very important."
    e "But Personal Wellbeing, as stated by the Hackathon Theme, is how well you treat yourself both mentally and physcially."
    e "This interactive little game is to showcase how a person can better put themselves at ease mentally by securing their online activities through building these tools."
    e "Overall, the tools I am going to present to you today is simple."
    e "I am going to show you how to create your own Github file repository, your own browser, and your own VPN."
    e "Please know that at anytime you feel like you want to go back to previous instructions, you can use your mouse to click the history function built into this engine to review the transcript!"
    e "ok, NOW LETS START!"
    












    #TASK 1: TUTORIAL ON CREATING GITHUB ACCOUNT

    show bg github_signup

    #creating a github
    e "First, I am going to show you how to create a Github account, which is used to serve as a repository for you save any small files you may need, especially of code."
    e "This is crucial as it allows you to have a backup of your code..."
    e "...that you can access at any time on a public or private repository depending on your needs."
    e "This allows you to store whatever files you need without fear of them being lost, although there is a file size limit, so it is mostly used for saving code...more on that later."
    e "First you will create a Github Account! From here, you will go to 'https://desktop.github.com' where this page will show up!"
    e "From here, you click on SIGN UP and register for an account."
    e "This is simple as creating a Username, Email Address, and Password!"

    hide bg github_signup
    show bg github_welcome_page

    e "After which, there will be this welcome page, which GitHub uses for studies."
    e "FINALLY, once you have reached this page, you have OFFICIALLY created a GitHub, which you can then download the Desktop Application to access..."
    e "...OR you can access it and 'push' files to your repositories in your browser."
    e "SPEAKING OF WHICH..."















    #TASK 2: TUTORIAL ON CREATING SECURE DOCKED BROWSER
    hide bg github_welcome_page
    image kasm1 = im.Scale("kasm_1.png", 1920, 1080)
    show kasm1 

    e "Now, creating a web browser is not easy"
    e "The method we are using here is using KASM workspaces"
    e "In other words, this browser is launched inside of a Docker container and then STREAMED to your web browser of choice."
    e "This method can be used on any computer greater than 2 CPU cores, 4GB of Memory and 50GB SSD storage being used as a server."
    e "however, for the purposes of this demonstration, we will use Ubuntu 22.04 version of Linux as the operating system of choice."
    e "Once getting into the Ubuntu desktop, To get started we will use this link here:"
    e "cd /tmp curl -0 https://kasm-static-content.s3.amazonaws.com/kasm_release_1.12.0.d4fd8a.tar.gz tar -xf kasm_release_1.12.0.d4fd8a.tar.gz sudo bash kasm_release/install.sh --accept-eula --swap-size 4096"
    
    image asl = im.Scale("asleep.jpg", 1920, 1080)
    show asl
    hide kasm1

    e "NOW, Don't get lost on me okay! It looks long but its not as bad as you think. What it is doing is grabbing the KASM 1.12 Release and installing it."
    image tm1 = im.Scale("terminal1.png", 1920, 1080)
    show tm1
    hide asl
    hide sophia
    e "This will take around a couple minutes to install on your server machine, "
    

    e "Once this is done, the Terminal will output the Kasm UI Login Credentials."
    hide tm1
    show terminal2


    e "Once done, find the reverse DNS Lookup, usually can be found through the 'dig -x ip_address' in the Linux Terminal"
    e "Afterwards, you post that string into your browser of choice, and you will find yourself in a Kasm's Workspaces UI"

    show kasm_2
    hide terminal2

    e "You will put in your Kasm UI login credentials that we had logged before, where you then click at the top where it says Workspaces"

    hide kasm_2
    show docker1

    e "And now you are in a Docked Container with the option to use any of the browsers seen on this UI"

    show docker2
    hide docker1
    e "You can use this browser just as a normal browser! Right here, we are using brave!"
    e "And when your are done searching the web in your docked web-browser, you just go to the side where it says Delete Session..."
    e "And then BAM your browser is closed!"
    e "You can even use a chrome extension to launch webpages directly from chrome into your docker."
    e "Now, this might feel like a massive waste of time....AND IT MIGHT BE....but its also a tool that..."
    e "once set up, allows you to have peace of mind that the browser you are using is self-contained and makes it so you can browse the web with peace of mind."
    e "No viruses are going to be able to download themselves onto your hardware and cause damage to you, so you can search the web in peace of mind."
    
    hide docker2
    show sophia

    e "However, the internet still has another challenge for us...time for us to create our own VPN"
    







    #TASK 3: TUTORIAL ON CREATING PERSONAL VPN
    
 #SUBSECTION: AMAZON WEB SERVICES FOR HOSTING
    e "Now, to actually make a VPN, we need to first work with AWS (Amazon Web Services) to start working in the cloud."
    
    hide sophia
    with dissolve
    show aws1
     
    e "First, we will go to https//aws.amazon.com and click on 'Create an AWS Account, where Amazon has multiple tier options for people just starting out."
    e "Personally, the one I recommend is the 750 Hour per month free for 12 Months. "
    e "They will ask you for a credit card, but DO NOT be scared. They won't charge you as long as you stay in the free tier."

    show aws2
    hide aws1

    e "After that, login in to the 'Console' and click that you are signing in as the root user."
    e "We will then launch a virtual machine right on the dashboard, under the options it is normally listed as EC2."

    show aws3
    hide aws2

    e "From there you can select the Amazon Machine Image, which is the operating system you will want to choose from"
    e "In our case, instead of doing that thought, what we wanna do is go to the AWS Marketplace on the side..."
    e "Which allows us to have pre-configured settings BEYOND the operating system"
    
    

 #SUBSECTION: CONFIGURE AWS for OpenVPN

    show aws4
    hide aws3

    e "In our case, AWS has an OpenVPN Access Server Option running on a Ubuntu distro of Linux. (Make sure its the free eligible version)"
    e "Once we choose our Free-eligible Instance Type, and Follow the On-Screen Instructions ll the way to 'Review and Launch' "

    show aws5
    hide aws4
    e "From here, you need to set up what is called a 'private-public' key pair, which is the type of authentication that AWS uses instead of a password"
    e "There should be a dropdown for to create a brand new key pair which you can also name."
    e "WARNING! DOWNLOAD THE KEY PAIR AS YOU WILL BE USING IT TO CONNECT TO THE VPN!"
    e "After downloading the key pair, you can now Launch Instances! And bring up your Virtual Machine"
    
    show aws6
    hide aws5
    e "Go to your instance listed, right click it, click connect, and copy the example ssh and paste it into your terminal of choice (Windows/Linux/Mac)"
    e "You now are Remoting into your Cloud Server! Congrats!"
    
    show awsterminal
    hide aws6

    e "Now, in the terminal again, all you have to do is do the following command: sudo passwd openvpn"
    e "Using this, we can just set our password for our VPN. After confirming password, our credentials for openvpn are set up"
    
    show aws7
    hide awsterminal

    e "Going to the AWS website we have open, we want to copy-paste the IPv4 Public IP under our instance information"
  
    show openvpn1
    hide aws7

    e "Then you will take remote to it with copy pasting the link https://<IPv4 IP we Copied>:943/admin and that will take us to the OpenVPN login page!"
    e "logging in is easy as typing in 'openvpn' in the user name and the password you selected from before."
    e "Sometimes, you will need to refresh the page to get the page to proceed, fair warning!"
    
    show openvpn2
    hide openvpn1

    e "You will now select the option under the configuration menu called VPN Settings..."

     
    show openvpn3
    hide openvpn2

    e "There should be an option that says 'Should client internet traffic be routed through the VPN?' and make sure that is YES. Save the settings, and then click 'Update Running Server'"

    hide openvpn3 
    show sophia 

    e "You now have a VPN server up and running! WOOOOOOO!"
    e "But wait...I feel like I'm missing something....."









 #SUBSECTION: Connecting to VPN
    e    "OH DUH! Now that we got the server running, we got connect to the VPN"

    hide sophia
    show openvpn4
    
    e "To do that, we once again go to 'https://<IPv4 IP we Copied>:943' and we will be connecting as a USER now instead of an admin."
    e "Thankfully, its the exact same credentials as before, so go ahead and login!"
   
    show openvpn5
    hide openvpn4

    e "You then download the client by clicking your operating system as shown on the screen!"
    e "After that, the client should download, click it to make sure to install it!"

    show openvpn6
    hide openvpn5
    e "You will then have an OpenVPN program running, just open it and connect to the pre-configure VPN by clicking on it"
    e "CONGRATZ YOU NOW HAVE A VPN"

    hide openvpn6











    #Conclusion: Why do We Want These Tools in the First Place

    show sophia
    e "Now, why did I go through all this trouble....well, the fact is the theme of this Hackathon is Personal Wellbeing. "
    e "Imagine that you found out that your identity had been stolen and cybercrime had left you in a financial crisis."
    e "The fact is that Mental and Physical Wellbeing can be directly related to Cybercrimes with a Tech-Influenced World."
    e "According to SafeHome.org, 21 Percent of Americans. YES, 21 PERCENT have been doxxed, or in layman terms, been maliciously targeted and had personal information published without consent."
    e "This same study found that 62 Percent of Americans personally knew of someone who had been doxxed online."

    # Source of Information: https://www.safehome.org/family-safety/doxxing-online-harassment-research/

    e "Also, latest statistics show that One in Two American internet users had their accounts breached in 2022."
    
    # Source of Information: https://aag-it.com/the-latest-cyber-crime-statistics/

    e "And the hypothestical situation of your identity being stolen? THATS NOT JUST CONJECTURE!"
    e "From Two-Thousand and Nineteen to Two-Thousand and Twenty, the United State exprienced a THREE HUNDRED AND ELEVEN PERCENT increase in identity theft, with a total pyout of Three Hundren Million USD."

    # Source of Information: https://www.consumeraffairs.com/finance/identity-theft-statistics.html

    e "In Two-Thousand and Twenty, a dramatic spike in cybercrime cases were reported..."
    e "...with upwards of Thirty-Four Point 5 Million Pounds STOLEN in pandemic scams as reported by the BBC."
    # Source of Information:https://www.bbc.co.uk/news/technology-56499886

    e "All of these tools are to prevent all of these burdens that create financial, physical, mental, and emotional strife, something that this program hopes to accomplish in a concisive manner."
    e "THANK YOU FOR PLAYING MY GAME! (YAHOOOOOOOOOOOOO!)"


    # This ends the game.
    return
