using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Enemy : MonoBehaviour
{

    [SerializeField]
    private float _speed = 4.0f;

    // "Player" is the script for the Player
    private Player _player;

    private Animator _animator;

    private AudioSource _audioSource;

    // Start is called before the first frame update
    void Start()
    {
        _player = GameObject.Find("Player").GetComponent<Player>();

        _audioSource = GetComponent<AudioSource>();

        if (_player == null)
        {
            Debug.LogError("The Player is NULL.");
        }

        _animator = gameObject.GetComponent<Animator>();

        if (_animator == null)
        {
            Debug.LogError("The Animator is NULL.");
        }

        if (_audioSource == null)
        {
            Debug.LogError("The Enemy's Audio Source is NULL.");
        }
    }

    // Update is called once per frame
    void Update()
    {
        // Move enemy down
        transform.Translate(Vector3.down * _speed * Time.deltaTime);

        // Sends Enemy to a random position at the top of the screen
        if (transform.position.y < -6.0f)
        {
            transform.position = new Vector3(Random.Range(-8f, 8f), 7f, 0);
        }
    }

    private void OnTriggerEnter2D(Collider2D other)
    {
        if (other.tag == "Player")
        {
            // Check if the player's script exists
            if (_player != null)
            {
                _player.Damage();
            }

            _animator.SetTrigger("OnEnemyDeath");
            _speed = 0;
            _audioSource.Play();

            Destroy(this.gameObject, 2.35f);
        }
        
        if (other.tag == "Laser")
        {
            Destroy(other.gameObject);

            // Check if the player's script exists
            if (_player != null)
            {
                _player.AddScore();
            }

            _animator.SetTrigger("OnEnemyDeath");
            _speed = 0;
            _audioSource.Play();

            Destroy(this.gameObject, 2.35f);
        }
    }
}
