using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Powerup : MonoBehaviour
{

    [SerializeField]
    private float _speed = 3.0f;

    // Powerup ID is assigned in Inspector
    [SerializeField] // 0 = Triple Shot, 1 = Speed, 2 = Shields
    private int _powerupID;

    [SerializeField]
    private AudioClip _powerupAudio;

    // Update is called once per frame
    void Update()
    {
        // Move power up down
        transform.Translate(Vector3.down * _speed * Time.deltaTime);

        // Delete power up when it is off screen
        if (transform.position.y < -5.0f)
        {
            Destroy(this.gameObject);
        }
    }

    private void OnTriggerEnter2D(Collider2D other)
    {
        if (other.tag == "Player")
        {
            // "Player" is the script for the Player
            Player player = other.transform.GetComponent<Player>();

            AudioSource.PlayClipAtPoint(_powerupAudio, transform.position);

            // Check if the players script exists
            if (player != null)
            {
                switch (_powerupID)
                {
                    case 0:
                        // Activate Triple Shot Power up
                        player.TripleShotActive();
                        break;
                    case 1:
                        // Activate Speed Power up
                        player.SpeedActive();
                        break;
                    case 2:
                        // Activate Shields Power up
                        player.ShieldsActive();
                        break;
                    default:
                        Debug.Log("Default Value");
                        break;
                }
            }

            

            Destroy(this.gameObject);
        }
    }
}
