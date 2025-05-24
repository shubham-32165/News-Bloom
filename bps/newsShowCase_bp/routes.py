from . import newsShowCase_bp
from .Controllers import newsShowCase, channelList

newsShowCase_bp.route('/')(newsShowCase)
newsShowCase_bp.route('/<channelName>')(channelList)