# 01. Strategy Pattern
## Overview
이 단원에서는 SimUdock 이라 불리는 오리 시뮬레이션 프로그램을 만들면서 strategy pattern 에 대해서 학습한다.
오리 시뮬레이션에서는 오리가 소리를 내고 (`quack`) 날고 (`fly`) 수영 (`swim`) 을 한다. 또한 오리의 종류를 나타낼 (`display`) 수 있다.
하지만, 시뮬레이션에서는 생명이 있는 오리가 아닌 다른 오리들이 존재할 수 있다. 예를 들면 Rubber Duck 이나 Decoy Duck 이 있다.
이 오리들은 소리를 내거나 날지 못한다. 하지만 Rubber Duck 은 소리는 낼 수 있지만 날지 못하고, Decoy Duck 은 소리를 낼 수도, 날 수도 없다. 모든 오리들이 단순히 `Duck` 이라는 상위 class 를 상속받을 경우, 생명이 없는 오리들에 대한 행동들을 개별적으로 구현해야하기 때문에, 코드의 중복이 일어날 수 있다. 따라서, 이를 방지하기 위해 strategy pattern 을 사용한다.

## Method
### Step 1.
**각 concrete class 별로 달라지지만 서로 공유하는 부분을 찾아내고 달라지지 않는 부분과 분리한다.**
이번 예제의 경우 `quack` 와 `fly` 가 달라지는 부분이고, `swim` 은 모든 오리에 대해 동일하게 적용되는 부분이다.
`display` 의 경우, 각 오리에 따라 다르게 구현되어져야하는 function 이다.

### Step 2.
**구현보다는 인터페이스에 맞춰서 프로그래밍한다.**
Step 1. 에서 분리된 *변하는* function 에 대해 각각 interface 를 따로 디자인한다. (`QuackBehavior`, `FlyBehavior`)
`Duck` 은 각 method 를 직접 가지는 대신, 따로 구현되어진 class 와 interface 를 통해 function 을 가진다. (`peform_quack`, `perform_fly`)

### Step 3.
이제 각 행동들과 그 행동을 개별적으로 가지는 오리들을 만들어 낸다.
`MallardDuck` 은 날 수 있고, Quack 소리를 낼 수도 있다 (`FlyWithWings`, `Quack`).
`RubberDuck` 은 날 수는 없지만, Squeak 소리를 낼 수는 있다 (`FlyNoWay`, `Squeak`).
`DecoyDuck` 은 날 수도, 소리를 낼 수도 없다 (`FlyNoWay`, `MuteQuack`).

## Note
* 클래스 사이의 관계를 생각해보자. (화살표로 나타내기)
  * A 는 B 이다. (inheritance)
  * A 에는 B 가 있다. (**composition**)
  * A 가 B 를 구현한다. (interface, abstraction)
* 디자인 패턴을 아는 것은 소통의 능력을 증가시킨다.
* Framework 나 library 는 구조를 만드는 데 도움을 주지 못한다. 하지만 디자인 패턴은 가능하다.
