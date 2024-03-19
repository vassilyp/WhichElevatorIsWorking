import sys
from bs4 import BeautifulSoup
 
def update_elevators(is_left_elevator_working, is_right_elevator_working):
    with open("index.html") as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    
    left_lift = soup.find(id="left-lift")
    right_lift = soup.find(id="right-lift")

    if is_left_elevator_working:
        left_lift['class'] = 'elevator working'
    else:
        left_lift['class'] = 'elevator'

    if is_right_elevator_working:
        right_lift['class'] = 'elevator working'
    else:
        right_lift['class'] = 'elevator'

    soup.find(id="left-lift").replace_with(left_lift)
    soup.find(id="right-lift").replace_with(right_lift)
    
    with open("index.html", "w") as outf:
        outf.write(str(soup.prettify()))

if __name__ == "__main__":
    a = str(sys.argv[1])
    b = str(sys.argv[2])

    is_left_lift_working = a.lower() == "true"
    is_right_lift_working = b.lower() == "true"

    update_elevators(is_left_lift_working, is_right_lift_working)