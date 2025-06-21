'''
using UnityEngine;

public class playerMoveMent : MonoBehaviour {

    public float speed = 5f;
    public ChracterController _cc;

    public void Awake() {
        _cc = GetComponent<ChracterController>(); }

    public void Update() {
        Vector3 moveDirection = new Vector(Input.GetAxisRaw("Horizental"), 0, Input.GetAxisRaw("Vertical"))
        _cc.Move(moveDirection(speed * Time.deltaTime))
        transform.LookAt(transfrom.Position + moveDirection) }
        
    }
'''

from turtle import *

d = 10
def turn_right():
    setheading(0)
    fd(d)

def turn_up():
    setheading(90)
    fd(d)

def turn_left():
    setheading(180)
    fd(d)

def turn_down():
    setheading(270)
    fd(d)

def blank():
    clear()

def keyboard():
    shape("turtle")
    speed(0)
    onkeypress(turn_right, "Right")
    onkeypress(turn_up, "Up")
    onkeypress(turn_left, "Left")
    onkeypress(turn_down, "Down")
    onkeypress(blank, "Escape")
    listen()

def mouse():
    speed(0)
    pensize(2)
    onscreenclick(goto)
    onkeypress(blank, "Escape")
    listen()

# Main
select = input("키보드(1) 마우스(2) : ")

if select == "1":
    keyboard()
elif select == "2":
    mouse()
