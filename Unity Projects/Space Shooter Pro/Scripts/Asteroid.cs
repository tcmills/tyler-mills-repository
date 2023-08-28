using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Asteroid : MonoBehaviour
{

    [SerializeField]
    private float _rotateSpeed = 8.0f;

    [SerializeField]
    private GameObject _explosionPrefab;

    // "Player" is the script for the Player
    private Player _player;

    private SpawnManager _spawnManager;

    // Start is called before the first frame update
    void Start()
    {
        _player = GameObject.Find("Player").GetComponent<Player>();

        if (_player == null)
        {
            Debug.LogError("The Player is NULL.");
        }

        // "SpawnManager" is the script for the Spawn_Manager
        _spawnManager = GameObject.Find("Spawn_Manager").GetComponent<SpawnManager>();

        if (_spawnManager == null)
        {
            Debug.LogError("The Spawn Manager is NULL.");
        }
    }

    // Update is called once per frame
    void Update()
    {
        transform.Rotate(new Vector3(0, 0, 1) * _rotateSpeed * Time.deltaTime);
    }

    private void OnTriggerEnter2D(Collider2D other)
    {
        if (other.tag == "Player")
        {
            //this.gameObject.SetActive(false);

            // Check if the player's script exists
            if (_player != null)
            {
                Instantiate(_explosionPrefab, transform.position, Quaternion.identity);

                _player.Damage();
                _player.Damage();
                _player.Damage();
            }

            
            Destroy(this.gameObject, 0.25f);
        }

        if (other.tag == "Laser")
        {
            Destroy(other.gameObject);
            Instantiate(_explosionPrefab, transform.position, Quaternion.identity);
            _spawnManager.StartSpawning();
            Destroy(this.gameObject, 0.25f);
        }
    }
}
