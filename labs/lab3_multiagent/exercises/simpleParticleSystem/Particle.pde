
class Particle{
  PVector pos, vel, acc;
  float radius, lifespan;
  Particle(PVector pos, float radius, float lifespan){
    this.pos= pos.copy();
    this.vel = new PVector();
    this.acc = new PVector();
    this.radius=radius;
    this.lifespan=lifespan;
  }
  void update(){    
    this.vel.add(this.acc);
    this.pos.add(this.vel);
    this.acc.mult(0);
  }
  
  void applyForce(PVector force){    
    this.acc.add(force);    
  }
  
  void draw(){
    fill(255,lifespan);
    colorMode(HSB, 255);
    fill(200);
    noStroke();
    ellipse(this.pos.x, this.pos.y, this.radius, this.radius);    
  }
  boolean isDead(){
    if(this.lifespan>0)
    return false;
    else return true;
  }
}
