background { color rgb <0.0, 0.0, 0.0> }

light_source { <10,100,-100> color rgb <1.0,1.0,1.0> }
light_source { <10,100,100> color rgb <1.0,1.0,1.0> }

global_settings { ambient_light <1,1,1>*1 }

//camera { location <0, 70, -300> look_at  <0, 100, 2> }
camera { location <0, 70, -300> look_at  <100, 100, 2> rotate <0,0,45> }
// http://cronodon.com/PovRay/POVRAY_example.html
union{
  intersection{
   #declare R = 2;
   #declare r = 10;
   #declare L = 7;
   #declare P = 0.5;
   #declare controlEnd = 20;
   #declare controlEndPlusOne = 21;
   sphere_sweep { b_spline controlEndPlusOne
   #for (Cntr, 0, controlEnd, 1)
            <R*cos(Cntr),Cntr*L,R*sin(Cntr)>, r
    #end
          }
  cylinder{<0,0,0>,<0,600,0>, 200 translate <0,10,0>}
  }//intersection
  intersection{
    #declare R2 = 2;
    #declare r2 = 7;
    #declare L2 = 7;
    #declare P = 0.5;
    #declare RHalve = -10;//value at which I obtain the old radius
    sphere_sweep { b_spline controlEndPlusOne
   #for (Cntr, 0, controlEnd, 1)
            <R2*cos(Cntr),Cntr*L2,R2*sin(Cntr)>, r+(Cntr-RHalve)*(r2-r)/(controlEnd-RHalve)
    #end
          }
    cylinder{<0,-600,0>,<0,120,0>, 200 translate <0,10,0>}
    rotate <0,0,45>
    translate <0,L*controlEnd-7,0>
    }//intersection
    intersection{
    #declare R3 = 2;
    #declare r3 = 7;
    #declare L3 = 7;
    #declare P = 0.5;
    #declare RHalve = -10;//value at which I obtain the old radius
    sphere_sweep { b_spline controlEndPlusOne
   #for (Cntr, 0, controlEnd, 1)
            <R3*cos(Cntr),Cntr*L3,R3*sin(Cntr)>, r+(Cntr-RHalve)*(r3-r)/(controlEnd-RHalve)
    #end
          
          }
    cylinder{<0,-600,0>,<0,120,0>, 200 translate <0,10,0>}
    rotate <0,0,-45>
          translate <0,L*controlEnd-7,0>
    }//intersection

//pigment { rgb <0.5,0.5,0.7> transmit 0.3}
//finish { diffuse 0.9 ambient 0.5 phong 0.7 phong_size 20 reflection { 0.2 } }
split_union off
texture{ pigment{ color rgb<0.5,0.5,0.7>*1.0}
            normal { bumps 0.2 scale 1.05}
            finish { phong 0.5}
  } // end of texture
}//end union
//cylinder{<0,0,0>,<0,600,0>, 200 translate <0,10,0>}
//pigment { rgbt <2,1,0,0> }
//finish { ambient 0.5 phong 0.7 phong_size 20 reflection { 0.0 } }
//}//end intersection
// }
