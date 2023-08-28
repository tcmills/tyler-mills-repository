using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class UIManager : MonoBehaviour
{
    [SerializeField]
    private Text _scoreText;

    [SerializeField]
    private Image _LivesImg;
    [SerializeField]
    private Sprite[] _livesSprites;

    [SerializeField]
    private Text _gameOverText;
    [SerializeField]
    private Text _restartText;
    private GameManager _gameManager;

    // Start is called before the first frame update
    void Start()
    {
        _gameOverText.gameObject.SetActive(false);
        _scoreText.text = "Score: " + 0;
        _gameManager = GameObject.Find("Game_Manager").GetComponent<GameManager>();

        if (_gameManager == null)
        {
            Debug.LogError("Game Manager is NULL.");
        }
    }

    public void UpdateScore(int playerScore)
    {
        _scoreText.text = "Score: " + playerScore;
    }

    public void UpdateLives(int currentLives)
    {
        _LivesImg.sprite = _livesSprites[currentLives];

        if (currentLives < 1)
        {
            GameOverSequence();
        }
    }

    void GameOverSequence()
    {
        _gameManager.GameOver();
        _restartText.gameObject.SetActive(true);
        StartCoroutine(GameOverFlickerRoutine());
    }

    IEnumerator GameOverFlickerRoutine()
    {
        while (true)
        {
            _gameOverText.gameObject.SetActive(true);
            yield return new WaitForSeconds(1.0f);
            _gameOverText.gameObject.SetActive(false);
            yield return new WaitForSeconds(1.0f);
        }
    }
}
