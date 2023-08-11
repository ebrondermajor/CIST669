import xml.etree.ElementTree as ET

## this returns everything between the subfields in a line of the XML file so it can match
def clean(x):
    first=x.find("$")
    y=x[first+2:100]
    try:
        second=y.find("$")
        y=y[0:second]
    except TypeError:
        pass
    return(y)

## this just extracts the subfield code from the QLSP files
def code(x):
    first=x.find("$")
    y=x[first:first+2]
    return(y)

## looks at all of the subject headings for an individual record and provides a de-duped list of translations, matching on the 7xx field in the QLSP headings and returning the Spanish-language 1xx field
def translate(completeHeadings,qlsp):
    result=[]
    for y in completeHeadings:
        ssh=[]
        tag=y[0] 
        for i in range(3):
            y.remove(y[0])
        for i in range(1,len(y)):            
            if i%2==0:
                pass
            else:
                for x in range(len(qlsp)):
                    try:
                        if qlsp[x][1]=="7":
                            heading=clean(qlsp[x])
                            c=code(qlsp[x])
                            if y[i].strip(".")==heading:
                                if c==y[i-1]:
                                    if len(ssh)==0:
                                        if c=="$a":
                                            ssh.append(tag) 
                                            ssh.append("  #7 ")
                                            ssh.append(c)
                                            ssh.append(" ")
                                            sheading=qlsp[x-1][10:100].strip("\n")
                                            ssh.append(sheading)
                                        else:
                                            pass
                                    elif len(ssh)>1:
                                        ssh.append(" ")
                                        ssh.append(c)
                                        ssh.append(" ")
                                        sheading=qlsp[x-1][10:100].strip("\n")
                                        ssh.append(sheading)
                                        
                    except IndexError:
                        pass
                
                if len(ssh)>1 and ssh not in result:
                    result.append(ssh)
                else:
                    pass
                uniqueresult=[]
                for x in result:
                    if x not in uniqueresult:
                        uniqueresult.append(x)       
    return uniqueresult

## extracts any elements in the XML file that have a tag of 650 or 655
def extractHeadings(root,z):
    completeHeadings=[] 
    subjectheadings=["650","655"]
    for x in range(5,1000):
        try:
           if root[z][x].attrib["tag"] in subjectheadings:
               sh=[]
               sh.append(root[z][x].attrib["tag"])
               sh.append(root[z][x].attrib["ind1"])
               sh.append(root[z][x].attrib["ind2"])
               try:
                   for j in range(5):
                       sh.append("$"+root[z][x][j].attrib["code"])
                       sh.append(root[z][x][j].text)
               except IndexError:
                   pass
               completeHeadings.append(sh)
        except IndexError:
            pass
    return completeHeadings

def main():
    qlsptext=open("qlsp2.txt",encoding="utf8") ## substitute your file here
    qlsp=[]
    for i in qlsptext:
        qlsp.append(i)
    doc=input("Enter the name of the file with the MARC records to evaluate: ")
    tree = ET.parse(doc)
    root = tree.getroot()
    r=int(input("How many records are included in the XML file? "))
    for z in range(0,r):   
        try:
            completeHeadings=extractHeadings(root,z)
            print()    
            print("Existing subject headings in record ",root[z][1].text,":", sep="") 
            for y in completeHeadings:
                for x in y:
                    print(x,end=" ")
                print()
            print()
            print("Potential Spanish-language subject headings for record ",root[z][1].text,":", sep="")
            results=translate(completeHeadings,qlsp)
            for x in results:
                for z in x:
                    print(z,end="")
                print(". $2 qlsp") 
        except IndexError:
            pass

main()
