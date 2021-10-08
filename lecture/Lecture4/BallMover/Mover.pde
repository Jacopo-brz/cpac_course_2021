class Mover {

  PVector location; 
  PVector velocity;
  PVector acceleration;
  
  Mover() {
    location = new PVector(random(width), random(height)); //cartesian coordinates (pos_x,pos_y)
    velocity = new PVector(random(-2, 2), random(-2, 2));  //cartesian coordinates (vel_x,vel_y)
    acceleration = new PVector(0.1,-0.3);                  //cartesian coordinates (acc_x,acc_y)
  }

  void update() {
    location.add(velocity); //the next position given the velocity is computed in Processing as x2 = x1 + v
    velocity.add(acceleration); 
  }

  void display() {
    stroke(0);
    strokeWeight(2);
    fill(127);
    ellipse(location.x, location.y, 48, 48);
  }

  void checkEdges() { //if the ball exit the canvas --> go back to it

    if (location.x > width) {
      location.x = 0;
    } 
    else if (location.x < 0) {
      location.x = width;
    }

    if (location.y > height) {
      location.y = 0;
    } 
    else if (location.y < 0) {
      location.y = height;
    }
  }
}
