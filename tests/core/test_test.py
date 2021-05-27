from pathlib import Path

import rasa.core.test
from _pytest.capture import CaptureFixture
from rasa.core.agent import Agent


async def test_testing_warns_if_action_unknown(
    capsys: CaptureFixture,
    e2e_bot_agent: Agent,
    e2e_bot_test_stories_with_unknown_bot_utterances: Path,
):
    await rasa.core.test.test(
        e2e_bot_test_stories_with_unknown_bot_utterances, e2e_bot_agent
    )
    output = capsys.readouterr().out
    assert "Test story" in output
    assert "contains the bot utterance" in output
    assert "which is not part of the training data / domain" in output


async def test_testing_valid_with_non_e2e_core_model(core_agent: Agent):
    test_stories = """
    version: "2.0"
    stories:
    - story: Test with entity annotation
      steps:
      - intent: greet
        user: |-
           Hi, my name is [Anca]{"entity": "name"}
      - bot: hey there Anca!
"""
    result = await rasa.core.test.test(test_stories, core_agent)
    assert "report" in result.keys()
