using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MovingPlatformVertical : MonoBehaviour
{
    [SerializeField]
    private Transform _targetA;
    [SerializeField]
    private Transform _targetB;

    [SerializeField]
    private float _speed = 2.0f;

    private bool _switchDirection = false;

    // Update is called once per frame
    void FixedUpdate()
    {
        if (transform.position == _targetA.position)
        {
            _switchDirection = true;
        }
        else if (transform.position == _targetB.position)
        {
            _switchDirection = false;
        }

        if (!_switchDirection)
        {
            transform.position = Vector3.MoveTowards(transform.position, _targetA.position, _speed * Time.deltaTime);
        }
        else
        {
            transform.position = Vector3.MoveTowards(transform.position, _targetB.position, _speed * Time.deltaTime);
        }
    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.tag == "Player")
        {
            other.transform.parent = this.transform;
        }
    }

    private void OnTriggerExit(Collider other)
    {
        if (other.tag == "Player")
        {
            other.transform.parent = null;
        }
    }
}
