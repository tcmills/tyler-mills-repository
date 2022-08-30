using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player : MonoBehaviour
{
    [SerializeField]
    private float _speed = 5.0f;
    [SerializeField]
    private float _speedMultiplier = 2;

    [SerializeField]
    private GameObject _laserPrefab;
    [SerializeField]
    private GameObject _tripleShotPrefab;

    [SerializeField]
    private GameObject _shieldVisualizer;
    [SerializeField]
    private GameObject _thruster;
    [SerializeField]
    private GameObject _leftEngineFire;
    [SerializeField]
    private GameObject _rightEngineFire;
    [SerializeField]
    private GameObject _explosionPrefab;

    private int _randomWing;

    [SerializeField]
    private float _fireRate = 0.5f;
    private float _canFire = -1f;

    [SerializeField]
    private int _lives = 3;

    private SpawnManager _spawnManager;

    private UIManager _uiManager;

    [SerializeField]
    private AudioClip _laserShotAudio;
    [SerializeField]
    private AudioClip _explosionAudio;
    private AudioSource _audioSource;

    private bool _isTripleShotActive = false;
    private bool _isSpeedActive = false;
    private bool _isShieldsActive = false;

    [SerializeField]
    private int _score;

    // Start is called before the first frame update
    void Start()
    {
        transform.position = new Vector3(0, 0, 0);
        // "SpawnManager" is the script for the Spawn_Manager
        _spawnManager = GameObject.Find("Spawn_Manager").GetComponent<SpawnManager>();
        // "UIManager" is the script for the Canvas
        _uiManager = GameObject.Find("Canvas").GetComponent<UIManager>();

        _audioSource = GetComponent<AudioSource>();

        _randomWing = Random.Range(1, 3);

        if (_spawnManager == null)
        {
            Debug.LogError("The Spawn Manager is NULL.");
        }

        if (_uiManager == null)
        {
            Debug.LogError("The UI Manager is NULL.");
        }

        if (_audioSource == null)
        {
            Debug.LogError("The Player's Audio Source is NULL.");
        }
    }

    // Update is called once per frame
    void Update()
    {
        CalculateMovement();
        if (Input.GetKeyDown(KeyCode.Space) && Time.time > _canFire)
        {
            FireLaser();
        }
    }

    void CalculateMovement()
    {
        float horizontalInput = Input.GetAxis("Horizontal");
        float verticalInput = Input.GetAxis("Vertical");

        if (_isSpeedActive)
        {
            // Move Player at double speed
            transform.Translate(new Vector3(horizontalInput, verticalInput, 0) * _speed * _speedMultiplier * Time.deltaTime);
        }
        else
        {
            // Move Player
            transform.Translate(new Vector3(horizontalInput, verticalInput, 0) * _speed * Time.deltaTime);
        }

        // Clamp vertical movement
        transform.position = new Vector3(transform.position.x, Mathf.Clamp(transform.position.y, -4.0f, 6.0f), 0);

        // Allows Player to wrap around the left and right sides of the screen
        if (transform.position.x > 11.3f)
        {
            transform.position = new Vector3(-11.3f, transform.position.y, 0);
        }
        else if (transform.position.x < -11.3f)
        {
            transform.position = new Vector3(11.3f, transform.position.y, 0);
        }
    }

    void FireLaser()
    {
        // _canFire is the time when the Player is able to fire again
        _canFire = Time.time + _fireRate;

        if (_isTripleShotActive)
        {
            // Creates a Triple_Shot
            Instantiate(_tripleShotPrefab, transform.position, Quaternion.identity);
        }
        else
        {
            // Creates a laser that follows Laser.cs
            Instantiate(_laserPrefab, transform.position + new Vector3(0, 1.0f, 0), Quaternion.identity);
        }

        _audioSource.PlayOneShot(_laserShotAudio);
    }

    public void Damage()
    {
        if (_isShieldsActive)
        {
            _isShieldsActive = false;
            _shieldVisualizer.SetActive(false);
            return;
        }

        _lives--;

        if (_lives == 2)
        {
            if (_randomWing == 1)
            {
                _leftEngineFire.SetActive(true);
            }
            else if (_randomWing == 2)
            {
                _rightEngineFire.SetActive(true);
            }
            else
            {
                Debug.LogError("Range is too big.");
            }

            _audioSource.PlayOneShot(_explosionAudio);
        }

        if (_lives == 1)
        {
            if (_randomWing == 1)
            {
                _rightEngineFire.SetActive(true);
            }
            else if (_randomWing == 2)
            {
                _leftEngineFire.SetActive(true);
            }
            else
            {
                Debug.LogError("Range is too big.");
            }

            _audioSource.PlayOneShot(_explosionAudio);
        }

        _uiManager.UpdateLives(_lives);

        if (_lives < 1)
        {
            _spawnManager.OnPlayerDeath();
            Instantiate(_explosionPrefab, transform.position, Quaternion.identity);
            Destroy(this.gameObject, 0.25f);
        }
    }

    public void TripleShotActive()
    {
        _isTripleShotActive = true;
        StartCoroutine(TripleShotPowerDownRoutine());
    }

    IEnumerator TripleShotPowerDownRoutine()
    {
        yield return new WaitForSeconds(5.0f);
        _isTripleShotActive = false;
    }

    public void SpeedActive()
    {
        _isSpeedActive = true;
        StartCoroutine(SpeedPowerDownRoutine());
    }

    IEnumerator SpeedPowerDownRoutine()
    {
        _thruster.gameObject.transform.localScale += new Vector3(0.5f, 0.5f, 0.5f);
        _thruster.gameObject.transform.position -= new Vector3(0, 0.42f, 0);
        yield return new WaitForSeconds(5.0f);
        _isSpeedActive = false;
        _thruster.gameObject.transform.localScale -= new Vector3(0.5f, 0.5f, 0.5f);
        _thruster.gameObject.transform.position += new Vector3(0, 0.42f, 0);
    }

    public void ShieldsActive()
    {
        _isShieldsActive = true;
        _shieldVisualizer.SetActive(true);
    }

    public void AddScore()
    {
        _score += 10;
        _uiManager.UpdateScore(_score);
    }

}
