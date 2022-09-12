using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ObjectPool : MonoBehaviour
{

    public static ObjectPool SharedInstance;
    private List<GameObject> pooledObjects;
    public GameObject enemy;
    public GameObject speedUp;
    public GameObject bullet;
    public GameObject sidewing;
    private int amountToPool = 9;
    private int numSidewings;
    public float spawnTimeEnemy = 3.0f;
    public float spawnTimeSidewing = 3.0f;
    public float spawnTimeSpeedUp = 3.0f;
    public GameObject capsule;

    void Awake()
    {
        SharedInstance = this;
    }

    // Start is called before the first frame update
    void Start()
    {
        numSidewings = 0;
        pooledObjects = new List<GameObject>();
        addToPool(enemy);
        addToPool(enemy);
        addToPool(enemy);
        addToPool(speedUp);
        addToPool(speedUp);
        addToPool(speedUp);
        addToPool(bullet);
        addToPool(bullet);
        addToPool(bullet);
        StartCoroutine(SpawnEnemyRoutine());
        StartCoroutine(SpawnSpeedUpRoutine());
        StartCoroutine(SpawnSideWingRoutine());
    }

    // Update is called once per frame
    void Update()
    {

    }

    IEnumerator SpawnEnemyRoutine()
    {
        while (true)
        {
            yield return new WaitForSeconds(spawnTimeEnemy);
            getPooledObject("enemy");
        }
    }

    IEnumerator SpawnSpeedUpRoutine()
    {
        while (true)
        {
            yield return new WaitForSeconds(spawnTimeSpeedUp);
            getPooledObject("speedUp");
        }

    }

    IEnumerator SpawnSideWingRoutine()
    {
        while (true)
        {
            yield return new WaitForSeconds(spawnTimeSidewing);
            getPooledObject("sidewing");
        }
    }

    public void increasePool(int capacity)
    {
        amountToPool += capacity;
    }

    public void addToPool(GameObject gObject)
    {
        if (pooledObjects.Count == amountToPool)
        {
            increasePool(1);
        }

        GameObject temp = Instantiate(gObject);
        temp.SetActive(false);
        pooledObjects.Add(temp);
    }

    public void getPooledObject(string gObject)
    {
        if (gObject == "bullet")
        {
            for (int i = 0; i < pooledObjects.Count; i++)
            {
                if (!pooledObjects[i].activeInHierarchy && pooledObjects[i].tag == bullet.tag)
                {
                    pooledObjects[i].transform.position = capsule.transform.position;
                    pooledObjects[i].SetActive(true);
                    return;
                }
            }

            addToPool(bullet);
            getPooledObject("bullet");
        }

        if (gObject == "bullet0")
        {
            for (int i = 0; i < pooledObjects.Count; i++)
            {
                if (!pooledObjects[i].activeInHierarchy && pooledObjects[i].tag == bullet.tag)
                {
                    pooledObjects[i].transform.position = new Vector3(capsule.transform.position.x + 2, capsule.transform.position.y - 2, 0);
                    pooledObjects[i].SetActive(true);
                    return;
                }
            }

            addToPool(bullet);
            getPooledObject("bullet0");
        }

        if (gObject == "bullet1")
        {
            for (int i = 0; i < pooledObjects.Count; i++)
            {
                if (!pooledObjects[i].activeInHierarchy && pooledObjects[i].tag == bullet.tag)
                {
                    pooledObjects[i].transform.position = new Vector3(capsule.transform.position.x - 2, capsule.transform.position.y - 2, 0);
                    pooledObjects[i].SetActive(true);
                    return;
                }
            }

            addToPool(bullet);
            getPooledObject("bullet1");
        }

        if (gObject == "bullet2")
        {
            for (int i = 0; i < pooledObjects.Count; i++)
            {
                if (!pooledObjects[i].activeInHierarchy && pooledObjects[i].tag == bullet.tag)
                {
                    pooledObjects[i].transform.position = new Vector3(capsule.transform.position.x + 4, capsule.transform.position.y - 2, 0);
                    pooledObjects[i].SetActive(true);
                    return;
                }
            }

            addToPool(bullet);
            getPooledObject("bullet2");
        }

        if (gObject == "bullet3")
        {
            for (int i = 0; i < pooledObjects.Count; i++)
            {
                if (!pooledObjects[i].activeInHierarchy && pooledObjects[i].tag == bullet.tag)
                {
                    pooledObjects[i].transform.position = new Vector3(capsule.transform.position.x - 4, capsule.transform.position.y - 2, 0);
                    pooledObjects[i].SetActive(true);
                    return;
                }
            }

            addToPool(bullet);
            getPooledObject("bullet3");
        }

        if (gObject == "enemy")
        {
            for (int i = 0; i < pooledObjects.Count; i++)
            {
                if (!pooledObjects[i].activeInHierarchy && pooledObjects[i].tag == enemy.tag)
                {
                    pooledObjects[i].transform.position = new Vector3(Random.Range(-8f, 8f), 8.0f, 0);
                    pooledObjects[i].SetActive(true);
                    return;
                }
            }

            addToPool(enemy);
            getPooledObject("enemy");
        }

        if (gObject == "speedUp")
        {
            for (int i = 0; i < pooledObjects.Count; i++)
            {
                if (!pooledObjects[i].activeInHierarchy && pooledObjects[i].tag == speedUp.tag)
                {
                    pooledObjects[i].transform.position = new Vector3(Random.Range(-8f, 8f), 8.0f, 0);
                    pooledObjects[i].SetActive(true);
                    return;
                }
            }

            addToPool(speedUp);
            getPooledObject("speedUp");
        }

        if (gObject == "sidewing")
        {
            for (int i = 0; i < pooledObjects.Count; i++)
            {
                if (!pooledObjects[i].activeInHierarchy && pooledObjects[i].tag == sidewing.tag)
                {
                    pooledObjects[i].transform.position = new Vector3(Random.Range(-8f, 8f), 8.0f, 0);
                    pooledObjects[i].SetActive(true);
                    return;
                }
            }

            if (numSidewings < 4)
            {
                addToPool(sidewing);
                numSidewings += 1;
                getPooledObject("sidewing");
            }
        }
    }

    public void removeSidewing(GameObject sidewing)
    {
        for (int i = 0; i < pooledObjects.Count; i++)
        {
            if (pooledObjects[i].activeInHierarchy && pooledObjects[i].GetInstanceID() == sidewing.GetInstanceID())
            {
                pooledObjects.Remove(pooledObjects[i]);
                return;
            }
        }
    }

}
