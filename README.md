# CIST669
A project to suggest Spanish-language subject headings for MARC records with existing English-language subject headings

Input an XML file consisting of a known number of MARC records and the script will suggest fully-formatted subheadings sourced via QLSP. The QLSP headings were sourced from lcsh-es.org, which also has links to other files that could easily be used in this script if preferred: https://lcsh-es.org/links.html. For this project, I downloaded a UTF8 file with the headings and used MarcEdit 7.5 to convert it into a .txt file for ease of use. 

Here is a sample of the output:

Existing subject headings in record [control number for your record]:
650   0 $a Social skills in children $v Juvenile literature. 
650   0 $a Attitude (Psychology) $v Juvenile literature. 
650   1 $a Attitude (Psychology) 

Potential Spanish-language subject headings for record 1633715 [control number for your record]:
650  #7 $a Actitud (Psicología) $v Literatura juvenil. $2 qlsp
650  #7 $a Actitud (Psicología). $2 qlsp

