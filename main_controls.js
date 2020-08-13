var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );

var renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

var geometry = new THREE.BoxGeometry();
var material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } );
var cube = new THREE.Mesh( geometry, material );

scene.add( cube );

camera.position.z = 5;


var animate = function (x_pos,y_pos,z_pos) {
  requestAnimationFrame( animate );
  //console.log(x_pos);
  cube.position.set(0,0,0);
  cube.rotation.x += 0.01;
  cube.rotation.y += 0.01;

  renderer.render( scene, camera );
};

function new_object(obj_name){
  var new_cube = new THREE.Mesh( geometry, material );
  new_cube.name = obj_name;
};

function if_obj_exists(obj_name){
  console.log( scene.getObjectByName(obj_name) );
};

function my_animate (x_pos,y_pos,z_pos){
  console.log("my animate");
  //requestAnimationFrame( animate );
  //console.log(x_pos);
  cube.position.set(x_pos,y_pos,z_pos);
  //cube.rotation.x += 0.01;
  //cube.rotation.y += 0.01;

  renderer.render( scene, camera );
};

//animate(0,0,0);
//my_animate(0,0,0);

//self add
var ws = new WebSocket('ws://localhost:9000');
ws.onopen = function() {
    console.log('onopen');
};
ws.onmessage = function (event) {
    var msg = JSON.parse(event.data);
    console.log(msg);
    //console.log(msg["x"]);
    //cube.position.x=(msg["x"]);
    my_animate(msg["x"],msg["y"],msg["z"])
};
//self add complete
