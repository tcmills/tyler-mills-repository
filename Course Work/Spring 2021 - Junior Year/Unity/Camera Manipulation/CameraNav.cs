using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraNav : MonoBehaviour
{

    float RotationY = 0f;
    float RotationX = 0f;
    Vector3 oldPosition;

    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {

        Vector3 currentMouse = Input.mousePosition;

        if (Input.GetMouseButton(1))
        {
            RotationX += Input.GetAxis("Mouse X") * 2;
            RotationY += Input.GetAxis("Mouse Y") * -1 * 2;
            Camera.main.transform.localEulerAngles = new Vector3(RotationY, RotationX);
        }

        if (Input.GetMouseButtonDown(2))
        {
            oldPosition = currentMouse;
        }
        else if (Input.GetMouseButton(2))
        {
            Vector3 newPosition = Camera.main.ScreenToViewportPoint(oldPosition - currentMouse);
            Vector3 translation = new Vector3(newPosition.x * 2 * 2 * 2, newPosition.y * 2 * 2 * 2, 0);
            Camera.main.transform.Translate(translation, Space.Self);
            oldPosition = currentMouse;
        }

        Camera.main.transform.position += Input.GetAxis("Mouse ScrollWheel") * transform.forward * 2;

    }
}
