using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Bullet : MonoBehaviour
{

    private float speed = 5.0f;

    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        if (transform.position.y > 9.0f)
        {
            this.gameObject.SetActive(false);
        } else
        {
            transform.Translate(Vector3.up * speed * Time.deltaTime);
        }
    }
}
