using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SpeedUp : MonoBehaviour
{

    public float speed = 2.0f;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (transform.position.y < -9.0f)
        {
            this.gameObject.SetActive(false);
        }
        else
        {
            transform.Translate(Vector3.down * speed * Time.deltaTime);
        }
    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.tag == "Capsule")
        {
            Capsule capsule = other.transform.GetComponent<Capsule>();
            capsule.changeFireRate();
            this.gameObject.SetActive(false);
        }

        if (other.tag == "MiniShip")
        {
            Capsule capsule = GameObject.Find("Capsule").GetComponent<Capsule>();
            capsule.changeFireRate();
            this.gameObject.SetActive(false);
        }
    }
}
