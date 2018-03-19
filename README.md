# Salt-Framework
A very simple python script allowing easy access to your favorite pen-testing tools.

To add a new tool to the framwork, simply clone your desired tool into the libraries folder.

Within the SaltFramwork.py I have included some example layouts of some popular tools to give a clear idea of how to integrate your own, but heres a rundown of how to use the framwork.

! Keep in mind, while I have alot of tools listed, they will not work unless they are structurely cloned into directories as listed within the SaltFramework.py file. The code only comes with a test.py file, meant to show you how the code operates. !

First step - Clone the wanted tool into the libraries folder

2nd step - Create a menu entry under the "Create Menu" divider of the SaltFramework.py file.

3rd Step - Assign a variable name for the script to check for, the syntax is as follows.
  "STRINGNAME" = "Code required to run the program " +AKAMANTO
      the AKAMANTO string calls the second raw_input handler, which allows you to specify arguements for tools such as mitmf.
     
4th Step - Assign a path under the "Uses action as per selected" portion.
  This is where the variable we just created comes into play.. The code written here tells the script where your tools are located, along with what to listen for. 
  
And thats it !

It truly seems alot harder than it is, simply by looking at the code for 10 mins should easily be long enough to figure out my methods. 

Go wild and be free my children.
