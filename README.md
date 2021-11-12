<h1 align="center">Rasa Open Source</h1>

<div align="center">

[![Join the chat on Rasa Community Forum](https://img.shields.io/badge/forum-join%20discussions-brightgreen.svg)](https://forum.rasa.com/?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![PyPI version](https://badge.fury.io/py/rasa.svg)](https://badge.fury.io/py/rasa)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/rasa.svg)](https://pypi.python.org/pypi/rasa)
[![Build Status](https://github.com/RasaHQ/rasa/workflows/Continuous%20Integration/badge.svg)](https://github.com/RasaHQ/rasa/actions)
[![Coverage Status](https://coveralls.io/repos/github/RasaHQ/rasa/badge.svg?branch=main)](https://coveralls.io/github/RasaHQ/rasa?branch=main)
[![Documentation Status](https://img.shields.io/badge/docs-stable-brightgreen.svg)](https://rasa.com/docs)
![Documentation Build](https://img.shields.io/netlify/d2e447e4-5a5e-4dc7-be5d-7c04ae7ff706?label=Documentation%20Build)
[![FOSSA Status](https://app.fossa.com/api/projects/custom%2B8141%2Fgit%40github.com%3ARasaHQ%2Frasa.git.svg?type=shield)](https://app.fossa.com/projects/custom%2B8141%2Fgit%40github.com%3ARasaHQ%2Frasa.git?ref=badge_shield)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/orgs/RasaHQ/projects/23)

</div>

<a href="https://grnh.se/05a908c02us" target="_blank"><img align="center" src="https://www.rasa.com/assets/img/github/hiring_banner.png" alt="An image with Sara, the Rasa mascot, standing next to a roadmap with future Rasa milestones: identifying unsuccessful conversations at scale, continuous model evaluation, controllable NLG and breaking free from intents. Are you excited about these milestones? Help us make these ideas become reality - we're hiring!" title="We're hiring! Learn more"></a>

<hr />


💡 **Rasa 오픈 소스 3.0이 출시됩니다!** 💡


3.0의 아키텍처 변경 작업을 수행하는 동안 마이너 릴리즈를 잠시 중단해야 하기 때문에 [2.8](https://github.com/RasaHQ/rasa/milestone/39)은 2.x 시리즈의 마지막 마이너 버전이 될 것입니다. 당신은 3.0과 함께 출시할 예정인 새로운 기능과 개선 사항에 계속 기여할 수 있습니다. [컨트리뷰터 가이드라인](#how-to-contribute)에 대해서 자세히 알아보세요.

빠른 피드백을 받기 위해 앞으로 몇 달 동안 알파 릴리즈와 릴리즈 후보를 출시할 계획입니다. 계속 지켜봐 주세요!
<hr />

<img align="right" height="244" src="https://www.rasa.com/assets/img/sara/sara-open-source-2.0.png" alt="An image of Sara, the Rasa mascot bird, holding a flag that reads Open Source with one wing, and a wrench in the other" title="Rasa Open Source">
Rasa는 텍스트 및 음성 기반 대화를 자동화하는 오픈소스 머신러닝 프레임워크입니다. Rasa를 사용하면 다음과 같은 상황별 기능을 구축할 수 있습니다:<br/><br/>
- 페이스북 메신저(Facebook Messenger)<br />
- 슬랙(Slack)<br />
- 구글 행아웃(Google Hangouts)<br />
- 웹엑스 팀즈 (Webex Teams)<br />
- 마이크로소프트 봇 프레임워크(Microsoft Bot Framework)<br />
- 로켓챗(Rocket.chat)<br />
- 매터모스트(Mattermost)<br />
- 텔레그램(Telegram)<br />
- 트윌리오(Twilio)<br />
- 나만의 맞춤 대화 채널<br /><br />


또는 다음과 같은 음성 비서를 구축할 수 있습니다:
- 알렉사 스킬(Alexa Skills)
- 구글 홈 액션(Google Home Actions)

Rasa는 많은 대화를 주고받을 수 있는 상황별 어시스턴트를 구축하는 데 도움이 됩니다.사람이 상황에 따라 비서와 의미 있는 교환을 하려면 비서가 상황을 이용하여 이전에 논의된 내용을 구축할 수 있어야 합니다. Rasa를 사용하면 확장 가능한 방식으로 이를 수행할 수 있는 비서를 구축할 수 있습니다.

이 [블로그 게시물](https://medium.com/rasa-blog/a-new-approach-to-conversational-software-2e64a5d05f2a)에는 더 많은 배경 정보를 확인할 수 있습니다. 


---
- **Rasa는 무엇을 하나요? 🤔**
  [우리 웹사이트를 확인하세요](https://rasa.com/)

- **나는 Rasa를 처음 사용합니다 😄**
  [Rasa 시작하기](https://rasa.com/docs/getting-started/)

- **자세한 문서를 읽어보고 싶습니다 🤓**
  [문서 읽어보기](https://rasa.com/docs/)

- **Rasa를 설치할 준비가 되었습니다 🚀**
  [설치](https://rasa.com/docs/rasa/user-guide/installation/)

- **Rasa 사용법을 배우고 싶어요 🚀**
  [튜토리얼](https://rasa.com/docs/rasa/user-guide/rasa-tutorial/)

- **질문이 있어요 ❓**
  [Rasa 커뮤니티 포럼](https://forum.rasa.com/)

- **기여하고 싶어요 🤗**
  [기여 방법](#how-to-contribute)

---
## 도움을 받을 수 있는 곳

[Rasa Docs](https://rasa.com/docs/rasa).에는 광범위한 문서들이 있습니다. 설치한 버전에 대한 문서를 볼 수 있도록 올바른 버전을 선택했는지 확인하세요.

질문에 대한 빠른 답변은 [Rasa 커뮤니티 포럼](https://forum.rasa.com)을 이용해주세요.

### README 내용:
- [기여하는 방법](#how-to-contribute)
- [개발 내부 내용](#development-internals)
- [출시](#releases)
- [라이센스](#license)

### how-to-contribute
우리는 귀하의 기여를 이 레포지토리에 merge할 수 있게 되어 매우 기쁩니다!

pull 요청을 통해 기여하려면 다음 단계를 따르세요:


1. 작업하려는 기능을 설명하는 issue를 만듭니다 (또는
    [컨트리뷰터 보드](https://github.com/orgs/RasaHQ/projects/23)을 참조하세요.)
2. 코드, 테스트 및 문서를 작성하고 ``black``으로 형식을 지정합니다
3. 변경 사항을 설명하는 pull request를 생성합니다

코드를 기여하는 방법에 대한 자세한 지침은 [코드 컨트리뷰터 가이드라인](CONTRIBUTING.md)을 확인하세요.

[저희 웹사이트](http://rasa.com/community/contribute)에서 Rasa에 기여하는 방법에 대한 자세한 정보를 찾을 수 있습니다. (
다른 많은 방법들도 가능합니다!) 

귀하의 풀 리퀘스트에 대한 검토는 유지 보수 담당자가 진행하며, 담당자가 필요한 변경 사항이나 질문에 대해 회신해 드릴 것입니다. 
또한 [컨트리뷰터 라이센스 계약](https://cla-assistant.io/RasaHQ/rasa)에 귀하의 서명을 요청할 것입니다.


## Development Internals

### Poetry 설치

Rasa는 패키징과 의존성 관리를 위해 Poetry를 사용합니다. 원본에서 빌드하고 싶다면, 먼저 Poetry를 설치해야 합니다. 설치 방법:

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

Poetry를 설치하는 몇 가지 다른 방법도 있습니다. 가능한 모든 옵션을 보려면 [공식 가이드](https://python-poetry.org/docs/#installation)를 확인하십시오.

### 환경 관리

공식 [Poetry 가이드](https://python-poetry.org/docs/managing-environments/)에서는 파이썬 버전 간에 쉽게 전환할 수 있도록 [pyenv](https://github.com/pyenv/pyenv) 또는 다른 비슷한 도구를 사용할 것을 제안합니다. 설치 방법: 

```bash
pyenv install 3.7.9
pyenv local 3.7.9  # 현재 프로젝트에 대해 파이썬 3.7.9 활성화
```
*주의*: 특정 버전의 파이썬을 설치하는 데 문제가 있는 경우 지원되는 다른 버전을 사용하십시오.

기본적으로, Poetry는 현재 활성화된 파이썬 버전을 사용하여 현재 프로젝트의 가상 환경을 자동으로 생성하려고 시도 할 것입니다. 가상 환경을 수동으로 만들고 활성화할 수도 있습니다. — 이 경우, Poetry는 그것을 dependencies를 설치하는데 사용해야 합니다. 예를 들어:

```bash
python -m venv .venv
source .venv/bin/activate
```

실행을 통해 환경이 선택되었는지 확인할 수 있습니다

```bash
poetry env info
```

### 원본에서 빌드

편집 가능한 모드에서 dependencies와 `rasa`를 설치하려면

```bash
make install
```

*macOS 유저라면*: macOS Big Sur에 dependencies에 대한 몇가지 컴파일러 문제가 있습니다.
. 설치 전에 `export SYSTEM_VERSION_COMPAT=1` 사용하면 도움이 될 것입니다.

### documentation 실행 및 변경

먼저, 필요한 모든 dependencies를 설치하십시오:

```bash
make install install-docs
```

설치가 완료되면 아래 코드를 사용하여 문서를 실행하고 볼 수 있습니다.

```bash
make livedocs
```

브라우저에 있는 문서의 로컬 버전으로 새 탭을 열여야 합니다;
열지 못했다면, 브라우저에서 http://localhost:3000 에 접속하십시오.
이제 문서를 로컬에서 변경할 수 있으며 웹 페이지가 자동으로 로드되어 변경 내용을 적용합니다.

### 테스트 실행

테스트를 실행하려면, 먼저 개발 요구 사항이 설치되어 있는지 확인하십시오:

```bash
make prepare-tests-ubuntu # Ubuntu, Debian based systems에서만
make prepare-tests-macos  # macOS에서만
```

그리고, 테스트를 실행하세요:

```bash
make test
```

시간을 절약하기 위해 여러 작업을 실행할 수 있습니다:

```bash
JOBS=[n] make test
```

`[n]`은 원하는 작업의 개수입니다. 생략할 경우, `[n]`은 pytest를 통해 자동으로 선택됩니다.


### 통합 테스트 실행

통합 테스트를 실행하려면, 개발 요구 사항이 설치되어 있는지 확인해야 합니다:

```bash
make prepare-tests-ubuntu # Ubuntu, Debian based systems에서만
make prepare-tests-macos  # macOS에서만
```

그런 다음, [Docker Compose](https://docs.docker.com/compose/install/)를 사용하는 다음 명령으로 서비스를 시작해야 합니다:

```bash
make run-integration-containers
```

마지막으로, 다음과 같은 통합 테스트를 실행할 수 있습니다:

```bash
make test-integration
```


### 병합 충돌 해결

Poetry에는 기본적으로 잠금 파일 `poetry.lock`의 병합 충돌을 해결하는 데 도움이 되는 솔루션이 포함되어 있지 않습니다.
그러나, [poetry-merge-lock](https://poetry-merge-lock.readthedocs.io/en/latest/)라는 좋은 도구가 있습니다.
설치 방법입니다:

```bash
pip install poetry-merge-lock
```

`poetry.lock`에서 병합 충돌을 자동으로 해결하려면 이 명령을 실행하십시오:

```bash
poetry-merge-lock
```

### 도커 이미지 로컬 작성

로컬 컴퓨터에 도커 이미지를 작성하려면 다음 명령을 실행하십시오:

```bash
make build-docker
```

도커 이미지는 로컬 컴퓨터에서 `rasa:localdev`로 사용할 수 있습니다.

### 코드 스타일

표준화된 코드 스타일을 위해 포맷터 [black](https://github.com/ambv/black)을 사용합니다.
유형 주석이 올바른지 확인하기 위해 [pytype](https://github.com/google/pytype)을 사용합니다.
당신의 코드가 제대로 포맷되지 않았거나 Check되지 않았다면, GitHub가 빌드할 수 없습니다.

#### 서식 설정

모든 커밋에서 코드를 자동으로 포맷하려면 [pre-commit](https://pre-commit.com/)을 사용하십시오.
`pip install pre-commit`을 통해 설치하고 루트 폴더에서 `pre-commit install`을 실행하면 됩니다.
이렇게 하면 모든 커밋에서 파일을 재구성하는 후크가 저장소에 추가됩니다.

수동으로 설정하려면 `poetry install`을 통해 black을 설치하십시오.
파일을 다시 포맷하려면 아래 코드를 실행하십시오.
```
make formatter
```

#### 유형 확인

코드베이스에서 타입을 확인하려면 `poetry install`을 사용하여 `mypy`을 설치하십시오.
타입을 확인하려면 아래 코드를 실행하십시오.
```
make types
```

### 문서 업데이트 배포

우리는 `Docusaurus v2`를 사용하여 태그가 지정된 버전과 `main` 브랜치에 대한 문서를 작성합니다.
빌드되는 정적 사이트는 이 저장소의 `documentation` 브랜치로 푸시됩니다.

우리는 netlify로 사이트를 주최합니다. `main` 브랜치 빌드에서 (`.github/workflows/documentation.yml`를 확인하세요), 우리는 빌드된 문서를 `documentation` 브랜치로 푸시합니다. Netlify는 해당 브랜치가 변경될 때마다 자동으로 문서 페이지를 다시 배포합니다

## Releases
### Minor Releases를 위한 Release 시간표
**Rasa 오픈 소스의 경우 일반적으로 시간 기반 Release 특히 월간 Release를 사용합니다.**
이는 특정 날짜에 특정 버전의 Rasa Open Source를 release 하겠다고 미리 약속하고, 일부 기능이 준비되지 않았을 수 있기 때문에 release에서 무엇을 수행할지 100% 확신할 수 없다는 것을 의미합니다.

각 분기 초에 Rasa 팀은 모든 제품의 예상 Release 날짜를 검토하고 해당 분기에 계획된 예상 작업뿐만 아니라 제품 전반에 걸쳐 작업을 수행하는지 확인합니다.

**날짜가 정해지면 각 [마일스톤](https://github.com/RasaHQ/rasa/milestones)을 업데이트합니다.**

### major release / minor release cutting

#### release 일주일 전

1. **[마일스톤](https://github.com/RasaHQ/rasa/milestones)이 이미 존재하는지, 정확한 날짜에 예약되었는지 검토합니다.**
2. **마일스톤의 issues 와 PR을 살펴봅니다**: 우리가 옮길 예정인 Release Highlights에 적합해 보이나요? 뭔가 놓치고 있는 것처럼 보이나요?  모든 PR을 인식하는 것에 대해 걱정하지 않아도 됩니다. 그러나 잠시 동안 마일스톤을 평가하는 것이 유용합니다.
3. **Engineering Slack 채널에 메시지를 게시하여**, Rasa 팀에게 다음 release에 대해 컷팅하고 있음을 알리고 다음과 같이 알려 주십시오:
    1. 적절한 마일스톤에 대한 링크를 제공합니다.
    2. 모든 사용자에게 issue와 PR을 검토하고 마일스톤에 할당하도록 지시합니다.
    3. 모든 사용자에게 예상 Release 날짜를 알려줍니다.

#### Release 하루 전


1. **마일스톤을 검토하고 진행 중인 PR 병합의 상태를 평가합니다. 버그와 수정 사항에 대한 후속 조치를 취합니다.** 릴리스에서 제때에 수정할 수 없는 새로운 버그나 퇴보가 발생할 경우, Slack에서 이 문제에 대해 논의하고 앞으로 나아갈 방법을 결정해야 합니다. 병합할 준비가 되지 않은 경우 마일스톤에서 issue/PR을 제거하고 Slack에 있는 PR 소유자와 제품 관리자에게 통보합니다. issue/PR 소유자는 Release와 관련된 모든 문제를 전달할 책임이 있습니다. Release 연기는 edge case 시나리오로서 고려되어야 합니다.


#### Release 당일! 🚀

1. **하루를 시작할 때, Slack에 릴리스 당일이라고 알리는 간단한 메시지를 올리십시오!** release 처리 및 release 시작 시간(문제가 발생하여 지연될 수 있으므로 오후 4시 이전까지)에 대해 알려 주십시오. 이 메시지는 이른 아침 그리고 Release 단계를 진행하기 전에 게시되어야 하며, 사람들이 그들의 PR와 issue를 확인할 수 있는 충분한 시간을 주어야 합니다. 그렇게 해야 그들은 남은 일을 계획할 수 있습니다.Slack 메시지의 형식은 [여기](https://rasa-hq.slack.com/archives/C36SS4N8M/p1613032208137500?thread_ts=1612876410.068400&cid=C36SS4N8M)에서 찾을 수 있습니다. release 시간은 다른 사용자가 항상 필요한 단계를 그에 따라 계획할 수 있도록 투명하게 전달되어야 합니다. 더 큰 변화가 있을 경우 이를 전달해야 합니다.

2. 마일스톤이 비어 있는지 확인하세요 (모든 항목이 병합되었거나 다음 마일스톤으로 이동되었는지)

3. 마일스톤의 모든 작업이 완료되면 Slack에 Release 과정을 시작한다는 간단한 메시지를 게시합니다 (어떤 것이든 누락된 경우)

4. **이제 당신은 [Rasa 오픈소스 README](https://github.com/RasaHQ/rasa#steps-to-release-a-new-version)에 설명된 지침을 따라 release 할 수 있습니다!**

#### Major rlease 이후

major release가 완료된 후 [문서 업데이트를 완료하기 위한 지침](./docs/README.md#manual-steps-after-a-new-version)을 따르십시오.

### 새로운 버전을 release하는 단계
패키지가 GitHub Actions에 의해 빌드되고 배포되기 때문에 새로운 버전을 release 하는 것은 매우 간단합니다.

*Terminology*:
* micro release (버전의 세번째 부분 증가): 1.1.2 -> 1.1.3.
* minor release (버전의 두번째 부분 증가): 1.1.3 -> 1.2.0
* major release (버전의 첫번째 부분 증가): 1.2.0 -> 2.0.0

*Release 단계*:
1. 모든 종속성이 최신 상태인지 확인합니다 (**특히 Rasa SDK**)
    - Rasa SDK의 경우 먼저 [새로운 Rasa SDK release](https://github.com/RasaHQ/rasa-sdk#steps-to-release-a-new-version)를 만듭니다(새 Rasa SDK release와 Rasa SDK release 간의 버전 번호가 일치하는지 확인하십시오)
    - 새로운 Rasa SDK release를 사용하여 태그를 푸시하고 패키지가 [pypi](https://pypi.org/project/rasa-sdk/)로 나타나면 Rasa 레포지토리의 종속성을 해결할 수 있습니다(아래 참조).

2. minor release인 경우 새로운 release에 해당하는 새로운 branch를 만듭니다. 
  eg.
   ```bash
    git checkout -b 1.2.x
    git push origin 1.2.x
    ```
3. 컷팅을 원하는 branch로 전환합니다 (major인 경우 `main`, minors와 micros를 위한 브랜치인 경우 `<major>.<minor>.x`)
    - `pyproject.toml`의 `rasa-sdk` 항목을 새 release 버전으로 업데이트하고 `poetry update`를 실행합니다. 이렇게 하면 모든 종속성이 해결된 새 `poetry.lock` 파일이 생성됩니다.
    - `git commit -am "bump rasa-sdk dependency"` 를 사용하여 변경 사항을 적용하되 push는 하지 마십시오. 다음 단계에 따라 자동으로 픽업됩니다.
4. 만약 이 버전이 major release인 경우 [README](https://github.com/RasaHQ/rasa#actively-maintained-versions) 및 [문서](https://github.com/RasaHQ/rasa/blob/main/docs/docs/actively-maintained-versions.mdx)에서 현재 유지 관리 중인 버전 목록을 업데이트합니다.
5. `make release`를 실행합니다.
6. release branch에 대한 PR을 생성합니다 (e.g. `1.2.x`)
7. PR이 merge되면 새 release에 태그를 지정합니다. (이는 항상 release 브랜치에서 진행되어야 합니다) eg. using
    ```bash
    git checkout 1.2.x
    git pull origin 1.2.x
    git tag 1.2.0 -m "next release"
    git push origin 1.2.0
    ```
   GitHub는 이 태그를 빌드하고 빌드 아티팩트를 게시할 것입니다.
8. 모든 단계가 완료되고 모든 것이 잘 진행되면 우리는 회사의 Slack (`product` channel) 에 다음과 같은 [메시지](https://rasa-hq.slack.com/archives/C7B08Q5FX/p1614354499046600)가 자동으로 게시되는 것을 볼 수 있습니다.
9. 채널에 메시지가 표시되지 않으면 다음 사항들을 확인할 수 있습니다:
    - [Github Actions](https://github.com/RasaHQ/rasa/actions)에서 워크플로우를 확인하고 현재 release의 merge된 PR이 성공적으로 완료되었는지 확인합니다. PR을 쉽게 찾으려면 `event: push` 및 `branch: <version number>` 필터를 사용할 수 있습니다. (release 2.4의 예는 [여기](https://github.com/RasaHQ/rasa/actions/runs/643344876)에서 볼 수 있습니다.)
    - 워크플로우가 완료되지 않은 경우, 문제를 해결할 수 있도록 워크플로우를 다시 실행하세요
    - 문제가 지속되면 로그 파일도 확인하고 문제의 근본 원인을 찾아보세요
    - 그래도 여전히 오류를 해결할 수 없는 경우, 조사를 통해 유용한 정보를 제공하여 인프라 팀에 문의하세요
10.  메시지가 `product` 채널에 올바르게 게시된 후 `product-engineering-alerts` 채널에서도 [이와 같은](https://rasa-hq.slack.com/archives/C01585AN2NP/p1615486087001000) Rasa Open Source release와 관련된 경고가 있는지 확인합니다.
    
### Cutting a Micro release

Micro release는 버그 수정만 포함하기 때문에 컷팅이 더 간단합니다.

**Micro release를 자르기 위해 해야 할 일은 다음과 같습니다.**

1. 누군가 추가해야 할 중요한 수정 사항이 있는 경우를 대비하여 Slack의 엔지니어링 팀에 micro 컷팅을 계획하고 있음을 알립니다.
2. 사용할 release 브랜치에 버그 수정이 필요한지 확인하십시오. (예: `2.0.4` 마이크로를 컷팅하는 경우, 수정사항이 `2.0.x` release 브랜치에 있어야 합니다.) 모든 micro는 `.x`에서 가져와야합니다! 
3. Rasa Open Source micro를 release할 준비가 되면 브랜치를 확인하고 `make release`를 실행하고, 단계를 따르고 PR을 merge합니다.
4. PR이 들어오면 `.x` 브랜치를 다시 pull하고 태그를 push합니다!

### 능동적으로 유지관리되는 버전

우리는 최신 major release의 모든 minor 버전과 이전 major release의 최신 minor 버전을 적극적으로 유지 관리하고 있습니다.
현재 이는 다음 minor 버전이 버그 수정 업데이트를 받을 것을 의미합니다:
- 1.10
- 2.x의 모든 minor 버전

## License
Apache 라이센스 버전 2.0에 따라 라이센스가 부여됩니다.
저작권 2021 Rasa Technologies GmbH. [Copy of the license](LICENSE.txt).

프로젝트 종속성의 라이센스 목록은 하단에서 찾을 수 있습니다.
[Libraries Summary](https://libraries.io/github/RasaHQ/rasa).
