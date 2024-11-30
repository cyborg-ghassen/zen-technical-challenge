import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.152.2/build/three.module.js';  // Import  Three.js
import { GLTFLoader } from 'https://cdn.jsdelivr.net/npm/three@0.152.2/examples/jsm/loaders/GLTFLoader.js'; // Import GLTFLoader

document.addEventListener('DOMContentLoaded', () => {
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer();
    
    const viewer = document.getElementById('viewer');
    renderer.setSize(viewer.offsetWidth, viewer.offsetHeight);
    viewer.appendChild(renderer.domElement);

    const loader = new GLTFLoader();  
    loader.load('/static/css/character.gltf', (gltf) => {
        console.log("Model Loaded:", gltf);
        scene.add(gltf.scene);
        gltf.scene.position.set(0, 0, 0);
        gltf.scene.scale.set(1, 1, 1);  
    }, undefined, (error) => {
        console.error('An error occurred while loading the GLTF model:', error);
    });

    const light = new THREE.AmbientLight(0x404040); 
    scene.add(light);

    camera.position.set(0, 0, 5);  

    function animate() {
        requestAnimationFrame(animate);
        renderer.render(scene, camera);
    }

    animate();
});
