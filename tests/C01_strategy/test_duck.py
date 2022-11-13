import pytest

from C01_strategy.simuduck.duck import MallardDuck, RubberDuck, DecoyDuck, Duck
from C01_strategy.simuduck.fly_behavior import FlyRocketPowered


@pytest.mark.parametrize(
    "duck, display_str, quack_str, fly_str",
    [
        (MallardDuck(), "I'm a real Mallard duck\n", "Quack\n", "I'm flying!\n"),
        (RubberDuck(), "I'm a rubber duck\n", "Squeak\n", "I can't fly\n"),
        (DecoyDuck(), "I'm a decoy duck\n", "<< Silence >>\n", "I can't fly\n"),
    ]

)
def test_duck(
    duck: Duck,
    display_str: str,
    quack_str: str,
    fly_str: str,
    capsys,
):
    duck.display()
    captured = capsys.readouterr()
    assert captured.out == display_str

    duck.perform_quack()
    captured = capsys.readouterr()
    assert captured.out == quack_str

    duck.perform_fly()
    captured = capsys.readouterr()
    assert captured.out == fly_str

    duck.fly_behavior = FlyRocketPowered()
    duck.perform_fly()
    captured = capsys.readouterr()
    assert captured.out == "I'm flying with a rocket!\n"
