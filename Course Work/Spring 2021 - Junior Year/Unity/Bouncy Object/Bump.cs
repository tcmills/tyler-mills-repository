using System;
using UnityEngine;
using UnityEngine.UI;

public class Bump : MonoBehaviour {
    //These variabels are used to apply forces to the game object
    private float frictionalForce;
    private Vector3 remainingForce;
    private float appliedForceMultiplier;

    //This is the bounding box you should use to check whether the game object is still on screen
    private Bounds cameraBounds;

    //UI Elements to change stuff. These items are initialized in the Unity Editor
    public Text forceText;
    public Slider forceSlider;
    public Text frictionText;
    public Slider frictionSlider;


    // Start is called before the first frame update
    void Start() {//You should modify this function
        //In this function you should initialize cameraBounds to be the visible area the gameobject can move
        //and remainingForce should be initialized to 0.
        float distance = Mathf.Abs(Camera.main.transform.position.z - transform.position.z);
        cameraBounds = new Bounds(new Vector3(0, 1, 0), new Vector3(distance * Mathf.Tan(Camera.main.fieldOfView * 0.5f * Mathf.Deg2Rad) * 2f * Camera.main.aspect, distance * Mathf.Tan(Camera.main.fieldOfView * 0.5f * Mathf.Deg2Rad) * 2f, 20f));
        remainingForce = new Vector3(0, 0, 0);
    }

    // Update is called once per frame
    void Update() {//Modify thi sfunction
        //This function updates the UI
        updateUI();
        //in this function you should update the forces acting on the object

        transform.Translate(remainingForce * Time.deltaTime);

        if (Input.GetMouseButtonDown(0))
        {
            OnMouseDown();
        }

        if (Vector3.Distance(remainingForce, new Vector3(0, 0, 0)) > 0f)
        {
            remainingForce = remainingForce - (frictionalForce * remainingForce);
        }

        //in this function you should also check whether the object is in the bounding box

        bool inside = true;

        if (!cameraBounds.Contains(transform.position) && inside)
        {
            Vector3 reflection = new Vector3(cameraBounds.ClosestPoint(transform.position).x - transform.position.x, cameraBounds.ClosestPoint(transform.position).y - transform.position.y, 0);
            remainingForce = Vector3.Reflect(remainingForce, Vector3.Normalize(reflection));
            inside = false;
        } else
        {
            inside = true;
        }
    }

    //This is called whenver the game object is "clicked"
    private void OnMouseDown() {
        //This function casts a ray that figures out what point on the object was hit to apply force in the appropriate direction
        RaycastHit hit;
        Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
        if (Physics.Raycast(ray, out hit)) {
            AddForce(hit.point);//call helper function
        }
    }

    //This function adds force to the object
    void AddForce(Vector3 hitPoint) {
        //This just makes it stay in two dimensions
        hitPoint.z = transform.position.z;
        //This calculates the direction to apply the force
        Vector3 direction = (transform.position - hitPoint);
        remainingForce += direction * appliedForceMultiplier;
    }

    //This just updates the UI
    public void updateUI() {
        //Grabs values from the sliders
        appliedForceMultiplier = forceSlider.value;
        frictionalForce = frictionSlider.value;

        //Updates text from the 
        forceText.text = "Force Multiplier = " + String.Format("{0:0.##}", appliedForceMultiplier);
        frictionText.text = "Friction Coefficient = " + String.Format("{0:0.##}", frictionalForce);
    }
}
