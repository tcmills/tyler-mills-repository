using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ObjectBehavior : MonoBehaviour
{

    public Toggle translateToggle;
    public Toggle rotateToggle;
    public Toggle deleteToggle;
    public Button addCube;
    public GameObject cube;
    public GameObject selected;
    public float cameraDistanceZ;

    // Start is called before the first frame update
    void Start()
    {
        rotateToggle.isOn = false;
        deleteToggle.isOn = false;
        translateToggle.isOn = false;
    }

    // Update is called once per frame
    void Update()
    {

        if (Input.GetMouseButtonDown(0))
        {
            Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
            RaycastHit hit;
            if (Physics.Raycast(ray, out hit))
            {
                selected = hit.transform.gameObject;
                cameraDistanceZ = Camera.main.WorldToScreenPoint(selected.transform.position).z;
            }
        }

        if (Input.GetMouseButton(0))
        {
            if (translateToggle.isOn && selected != null)
            {
                Vector3 screenPosition = new Vector3(Input.mousePosition.x, Input.mousePosition.y, cameraDistanceZ);
                Vector3 newPosition = Camera.main.ScreenToWorldPoint(screenPosition);
                selected.transform.position = newPosition;
            }
            if (rotateToggle.isOn && selected != null)
            {
                selected.transform.RotateAround(Camera.main.transform.up, Input.GetAxis("Mouse X") * -0.3f);
                selected.transform.RotateAround(Camera.main.transform.right, Input.GetAxis("Mouse Y") * 0.3f);
            }
            if (deleteToggle.isOn)
            {
                Destroy(selected);
            }
        } 
        else
        {
            selected = null;
        }
    }

    public void summonCube()
    {
        Instantiate(cube, Camera.main.transform.position + Camera.main.transform.forward * 5, Quaternion.identity);
    }
}
