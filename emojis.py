def remove_emojis(text):
    """_summary_

    Args:
        string: 이모지를 제거할 텍스트입니다.


    Returns:
        string :  이모지가 제거된 텍스트. 새로운 이모지가 추가되면 유니코드 블록을 업데이트 해야함.
    """

    if text == None:
        return ' ' #네이버 블로그와 같은 경우, content 파싱이 안되는 경우가 존재하여 (js로 막아놓음) 공백일 시 변환처리/.
    #유니코드 공식홈페이지에서 가져온 이모지. 최다빈도로 사용되는 1543개 이모지 제거
    chars_to_remove = chars_to_remove = "🌸📞✅⭐🤗☺️✔■�😂😍🤣😊🙏💕😭😘😊🥰🎉🥳🍕🌮👍😀😃😄😁😆😅🤣😂🙃😉😊😇💋💌💘💝💖💗💓💞💕💟❣💔❤🧡💛💚💙💜🤎🖤🤍💯💢💥💫💦💨🕳💣💬👁️‍🗨️🗨 🗯 💭 💤🀄🃏🅰️🅱️🅾️🅿️🆎🆑🆒🆓🆔🆕🆖🆗🆘🆙🆚🈁🈂️🈚🈯🈲🈳🈴🈵🈶🈷️🈸🈹🈺🉐🉑🌀🌁🌂🌃🌄🌅🌆🌇🌈🌉🌊🌋🌌🌍🌎🌏🌐🌑🌒🌓🌔🌕🌖🌗🌘🌙🌚🌛🌜🌝🌞🌟🌠🌡️🌤️🌥️🌦️🌧️🌨️🌩️🌪️🌫️🌬️🌭🌮🌯🌰🌱🌲🌳🌴🌵🌶️🌷🌸🌹🌺🌻🌼🌽🌾🌿🍀🍁🍂🍃🍄🍅🍆🍇🍈🍉🍊🍋🍌🍍🍎🍏🍐🍑🍒🍓🍔🍕🍖🍗🍘🍙🍚🍛🍜🍝🍞🍟🍠🍡🍢🍣🍤🍥🍦🍧🍨🍩🍪🍫🍬🍭🍮🍯🍰🍱🍲🍳🍴🍵🍶🍷🍸🍹🍺🍻🍼🍽️🍾🍿🎀🎁🎂🎃🎄🎅🎆🎇🎈🎉🎊🎋🎌🎍🎎🎏🎐🎑🎒🎓🎖️🎗️🎙️🎚️🎛️🎞️🎟️🎠🎡🎢🎣🎤🎥🎦🎧🎨🎩🎪🎫🎬🎭🎮🎯🎰🎱🎲🎳🎴🎵🎶🎷🎸🎹🎺🎻🎼🎽🎾🎿🏀🏁🏂🏃🏄🏅🏆🏇🏈🏉🏊🏋️🏌️🏍️🏎️🏏🏐🏑🏒🏓🏔️🏕️🏖️🏗️🏘️🏙️🏚️🏛️🏜️🏝️🏞️🏟️🏠🏡🏢🏣🏤🏥🏦🏧🏨🏩🏪🏫🏬🏭🏮🏯🏰🏳️🏳️‍🌈🏴🏴‍☠️🏴󠁧󠁢󠁥󠁮󠁧󠁿🏴󠁧󠁢󠁳󠁣󠁴󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏵️🏷️🏸🏹🏺🐀🐁🐂🐃🐄🐅🐆🐇🐈🐉🐊🐋🐌🐍🐎🐏🐐🐑🐒🐓🐔🐕🐖🐗🐘🐙🐚🐛🐜🐝🐞🐟🐠🐡🐢🐣🐤🐥🐦🐧🐨🐩🐪🐫🐬🐭🐮🐯🐰🐱🐲🐳🐴🐵🐶🐷🐸🐹🐺🐻🐼🐽🐾🐿️👀👁️👁️‍🗨️👂👃👄👅👆👇👈👉👊👋👌👍👎👏👐👑👒👓👔👕👖👗👘👙👚👛👜👝👞👟👠👡👢👣👤👥👦👧👨👨‍✈️👨‍❤️‍👨👨‍❤️‍💋‍👨👨‍⚕️👨‍⚖️👨‍🌾👨‍🍳👨‍🎓👨‍🎤👨‍🎨👨‍🏫👨‍🏭👨‍👦👨‍👦‍👦👨‍👧👨‍👧‍👦👨‍👧‍👧👨‍👨‍👦👨‍👨‍👦‍👦👨‍👨‍👧👨‍👨‍👧‍👦👨‍👨‍👧‍👧👨‍👩‍👦👨‍👩‍👦‍👦👨‍👩‍👧👨‍👩‍👧‍👦👨‍👩‍👧‍👧👨‍💻👨‍💼👨‍🔧👨‍🔬👨‍🚀👨‍🚒👨‍🦰👨‍🦱👨‍🦲👨‍🦳👩👩‍✈️👩‍❤️‍👨👩‍❤️‍👩👩‍❤️‍💋‍👨👩‍❤️‍💋‍👩👩‍⚕️👩‍⚖️👩‍🌾👩‍🍳👩‍🎓👩‍🎤👩‍🎨👩‍🏫👩‍🏭👩‍👦👩‍👦‍👦👩‍👧👩‍👧‍👦👩‍👧‍👧👩‍👩‍👦👩‍👩‍👦‍👦👩‍👩‍👧👩‍👩‍👧‍👦👩‍👩‍👧‍👧👩‍💻👩‍💼👩‍🔧👩‍🔬👩‍🚀👩‍🚒👩‍🦰👩‍🦱👩‍🦲👩‍🦳👪👫👬👭👮👯👰👱👲👳👴👵👶👷👸👹👺👻👼👽👾👿💀💁💂💃💄💅💆💇💈💉💊💋💌💍💎💏💐💑💒💓💔💕💖💗💘💙💚💛💜💝💞💟💠💡💢💣💤💥💦💧💨💩💪💫💬💭💮💯💰💱💲💳💴💵💶💷💸💹💺💻💼💽💾💿📀📁📂📃📄📅📆📇📈📉📊📋📌📍📎📏📐📑📒📓📔📕📖📗📘📙📚📛📜📝📞📟📠📡📢📣📤📥📦📧📨📩📪📫📬📭📮📯📰📱📲📳📴📵📶📷📸📹📺📻📼📽️📿🔀🔁🔂🔃🔄🔅🔆🔇🔈🔉🔊🔋🔌🔍🔎🔏🔐🔑🔒🔓🔔🔕🔖🔗🔘🔙🔚🔛🔜🔝🔞🔟🔠🔡🔢🔣🔤🔥🔦🔧🔨🔩🔪🔫🔬🔭🔮🔯🔰🔱🔲🔳🔴🔵🔶🔷🔸🔹🔺🔻🔼🔽🕉️🕊️🕋🕌🕍🕎🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚🕛🕜🕝🕞🕟🕠🕡🕢🕣🕤🕥🕦🕧🕯️🕰️🕳️🕴️🕵️🕶️🕷️🕸️🕹️🕺🖇️🖊️🖋️🖌️🖍️🖐️🖕🖖🖤🖥️🖨️🖱️🖲️🖼️🗂️🗃️🗄️🗑️🗒️🗓️🗜️🗝️🗞️🗡️🗣️🗨️🗯️🗳️🗺️🗻🗼🗽🗾🗿😀😁😂😃😄😅😆😇😈😉😊😋😌😍😎😏😐😑😒😓😔😕😖😗😘😙😚😛😜😝😞😟😠😡😢😣😤😥😦😧😨😩😪😫😬😭😮😯😰😱😲😳😴😵😶😷😸😹😺😻😼😽😾😿🙀🙁🙂🙃🙄🙅🙆🙇🙈🙉🙊🙋🙌🙍🙎🙏🚀🚁🚂🚃🚄🚅🚆🚇🚈🚉🚊🚋🚌🚍🚎🚏🚐🚑🚒🚓🚔🚕🚖🚗🚘🚙🚚🚛🚜🚝🚞🚟🚠🚡🚢🚣🚤🚥🚦🚧🚨🚩🚪🚫🚬🚭🚮🚯🚰🚱🚲🚳🚴🚵🚶🚷🚸🚹🚺🚻🚼🚽🚾🚿🛀🛁🛂🛃🛄🛅🛋️🛌🛍️🛎️🛏️🛐🛑🛒🛠️🛡️🛢️🛣️🛤️🛥️🛩️🛫🛬🛰️🛳️🛴🛵🛶🛷🛸🛹🤐🤑🤒🤓🤔🤕🤖🤗🤘🤙🤚🤛🤜🤝🤞🤟🤠🤡🤢🤣🤤🤥🤦🤧🤨🤩🤪🤫🤬🤭🤮🤯🤰🤱🤲🤳🤴🤵🤶🤷🤸🤹🤺🤼🤽🤾🥀🥁🥂🥃🥄🥅🥇🥈🥉🥊🥋🥌🥍🥎🥏🥐🥑🥒🥓🥔🥕🥖🥗🥘🥙🥚🥛🥜🥝🥞🥟🥠🥡🥢🥣🥤🥥🥦🥧🥨🥩🥪🥫🥬🥭🥮🥯🥰🥳🥴🥵🥶🥺🥼🥽🥾🥿🦀🦁🦂🦃🦄🦅🦆🦇🦈🦉🦊🦋🦌🦍🦎🦏🦐🦑🦒🦓🦔🦕🦖🦗🦘🦙🦚🦛🦜🦝🦞🦟🦠🦡🦢🦴🦵🦶🦷🦸🦹🧀🧁🧂🧐🧑🧒🧓🧔🧕🧖🧗🧘🧙🧚🧛🧜🧝🧞🧟🧠🧡🧢🧣🧤🧥🧦🧧🧨🧩🧪🧫🧬🧭🧮🧯🧰🧱🧲🧳🧴🧵🧶🧷🧸🧹🧺🧻🧼🧽🧾🧿㊙️㊗️❤♫☎•°♨✈✣☏■☀➑✂☑✉☼☆✄✔✆—☁★♕✘№‰♠✪✝╳©…♥✰†✎®¶♦✧‡✍❆♣✦◑♀℮❅♤♡♪♂·★▶◆○＃＆＊＠§※☆★ㅁ9●◎◇◆□■△▲▽▼▷▶♤♠♡♥♧♣⊙◈▣◐◑☏☎☜☞㈜®ㅁㄻ"

    # 이모지 범위에 포함되지 않으며, 특정 문자 목록에도 포함되지 않는 문자를 추가로 제거.
    return ''.join(char for char in text
            if not (char.isascii() and 0x1F600 <= ord(char) <= 0x1F64F) and char not in chars_to_remove)


