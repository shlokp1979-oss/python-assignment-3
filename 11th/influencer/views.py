from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import InfluencerProfile
from .forms import InfluencerProfileForm


@login_required
def profile(request):

    profile, created = InfluencerProfile.objects.get_or_create(
        user=request.user,
        defaults={
            'display_name': request.user.username
        }
    )

    return render(
        request,
        'profile.html',
        {
            'profile': profile
        }
    )


@login_required
def edit_profile(request):

    profile, created = InfluencerProfile.objects.get_or_create(
        user=request.user,
        defaults={
            'display_name': request.user.username
        }
    )

    if request.method == 'POST':

        form = InfluencerProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = InfluencerProfileForm(instance=profile)

    return render(
        request,
        'edit_profile.html',
        {
            'form': form
        }
    )