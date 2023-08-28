using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Laser : MonoBehaviour
{

    [SerializeField]
    private float _speed = 8.0f;

    // Update is called once per frame
    void Update()
    {
        // Move laser up
        transform.Translate(Vector3.up * _speed * Time.deltaTime);

        if (transform.position.y >= 8.0f)
        {
            // If laser is a part of a Triple Shot, destroy the Triple Shot container as well
            if (transform.parent != null)
            {
                Destroy(transform.parent.gameObject);
            }

            Destroy(this.gameObject);
        }
    }
}
