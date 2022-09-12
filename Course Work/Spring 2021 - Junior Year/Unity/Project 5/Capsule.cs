using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Capsule : MonoBehaviour
{

    private float fireRate = 1.0f;
    private float nextFire = 0.0f;
    private ObjectPool pool;
    public float maxFireRate = 10f;
    private int shipID = 0;
    public GameObject miniShip;
    private GameObject newShip0;
    private GameObject newShip1;
    private GameObject newShip2;
    private GameObject newShip3;
    private bool ship0On = false;
    private bool ship1On = false;
    private bool ship2On = false;
    private bool ship3On = false;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        Vector3 currentMouse = Input.mousePosition;
        currentMouse.z = 10;
        Vector3 newPosition = Camera.main.ScreenToWorldPoint(currentMouse);
        this.transform.position = newPosition;

        if (Input.GetMouseButton(0) && Time.time > nextFire)
        {
            FireBullet();
        }

    }

    public void FireBullet()
    {
        nextFire = Time.time + (1.0f / fireRate);
        pool = GameObject.Find("SystemController").GetComponent<ObjectPool>();
        pool.getPooledObject("bullet");

        if (ship0On)
        {
            pool.getPooledObject("bullet0");
        }

        if (ship1On)
        {
            pool.getPooledObject("bullet1");
        }

        if (ship2On)
        {
            pool.getPooledObject("bullet2");
        }

        if (ship3On)
        {
            pool.getPooledObject("bullet3");
        }

    }

    public void changeFireRate()
    {
        if (fireRate < maxFireRate)
        {
            fireRate += 1f;
        }
        
    }

    public void addShip()
    {
        switch (shipID)
        {
            case 0:
                newShip0 = Instantiate(miniShip, new Vector3(this.transform.position.x + 2, this.transform.position.y - 2, 0), Quaternion.identity);
                newShip0.transform.parent = this.transform;
                ship0On = true;
                break;
            case 1:
                newShip1 = Instantiate(miniShip, new Vector3(this.transform.position.x - 2 , this.transform.position.y - 2, 0), Quaternion.identity);
                newShip1.transform.parent = this.transform;
                ship1On = true;
                break;
            case 2:
                newShip2 = Instantiate(miniShip, new Vector3(this.transform.position.x + 4, this.transform.position.y - 2, 0), Quaternion.identity);
                newShip2.transform.parent = this.transform;
                ship2On = true;
                break;
            case 3:
                newShip3 = Instantiate(miniShip, new Vector3(this.transform.position.x - 4, this.transform.position.y - 2, 0), Quaternion.identity);
                newShip3.transform.parent = this.transform;
                ship3On = true;
                break;
            default:
                Debug.Log("Default Value");
                break;
        }
        shipID += 1;
    }

}
